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
#uva = uva.dropna(subset=['Date', 'Total Player Load', 'Explosive Efforts', 'Position'])

# Create a 'Month' column
uva['Month'] = uva['Date'].dt.to_period('M').dt.to_timestamp()

# Group by Month and Position, and average key metrics
monthly_avg = uva.groupby(['Month', 'Position'], as_index=False).agg({
    'Player Load Per Minute': 'mean',
    'Explosive Efforts': 'mean'
})

fig_load = px.line(
    monthly_avg,
    x='Month',
    y='Player Load Per Minute',
    color='Position',
    markers=True,
    title='Monthly Average: Player Load Per Minute by Position'
)

fig_load.update_layout(
    xaxis_title='Month',
    yaxis_title='Avg Player Load Per Minute',
    hovermode='x unified',
     xaxis=dict(
        range=['2023-09-01', '2024-03-30']  # Set desired zoom window
    )
)

fig_load.show()



fig_effort = px.line(
    monthly_avg,
    x='Month',
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
