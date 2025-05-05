# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp
import plotly.express as px
# load data
c1 = pd.read_csv('catapult season 1.csv')
c2 = pd.read_csv('catapult season 2.csv')
# merge the two seasons using concat ignoring their individual indexes
uva = pd.concat([c1, c2], ignore_index=True)

#check for duplicates
duplicates = uva.duplicated()
print(f"Number of duplicates: {duplicates.sum()}")
#drop duplicates
uva = uva.drop_duplicates()
#check for missing values
missing_values = uva.isnull().sum()
#drop missing values
#uva = uva.dropna()

#keep only key features
key_vars = [
    'Total Player Load', 'Player Load Per Minute', 'Explosive Efforts', 'Session Total Jump', 'Session Jumps Per Minute', 'Total IMA', 'IMA/Min', 'Position', 'Date'
]
uva = uva[key_vars]

# Convert 'Date' to datetime
uva['Date'] = pd.to_datetime(uva['Date'], errors='coerce')

# Drop rows with missing critical data
uva = uva.dropna(subset=['Date', 'Total Player Load', 'Explosive Efforts', 'Position'])

# Create a 'Week' column (start of the week, e.g., Monday)
uva['Week'] = uva['Date'].dt.to_period('W').apply(lambda r: r.start_time)

# Group by Week and Position, and average key metrics
weekly_avg = uva.groupby(['Week', 'Position'], as_index=False).agg({
    'Player Load Per Minute': 'mean',
    'Explosive Efforts': 'mean'
})

fig_load = px.line(
    weekly_avg,
    x='Week',
    y='Player Load Per Minute',
    color='Position',
    markers=True,
    title='Monthly Average: Total Player Load by Position'
)

fig_load.update_layout(
    xaxis_title='Month',
    yaxis_title='Avg Total Player Load',
    hovermode='x unified',
     xaxis=dict(
        range=['2023-10-01', '2024-03-30']  # Set desired zoom window
    )
)

fig_load.show()



fig_effort = px.line(
    weekly_avg,
    x='Week',
    y='Explosive Efforts',
    color='Position',
    markers=True,
    title='Monthly Average: Explosive Efforts by Position'
)

fig_effort.update_layout(
    xaxis_title='Month',
    yaxis_title='Avg Explosive Efforts',
    hovermode='x unified',
     xaxis=dict(
        range=['2023-10-01', '2024-03-30']  # Set desired zoom window
    )
)

fig_effort.show()
