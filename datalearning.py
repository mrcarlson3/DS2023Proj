## Cleaning the data

# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy as sp

# load data
c1 = pd.read_csv('catapult season 1.csv')
c2 = pd.read_csv('catapult season 2.csv')
# merge the two seasons using concat ignoring their individual indexes
df = pd.concat([c1, c2], ignore_index=True)

###
#check for duplicates
duplicates = df.duplicated()
duplicates.sum()
#drop duplicates
df = df.drop_duplicates()



#keep only key features
key_vars = [
    'Total Player Load', 'Player Load Per Minute', 'Explosive Efforts', 'Session Total Jump', 'Session Jumps Per Minute', 'Total IMA', 'IMA/Min', 'Position', 'Date', 'Period Number'
]
df = df[key_vars]

# converting date feature to datetime format so it can be used as time
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%y', errors='coerce')


# Creating a month column based on the date column
df['Month'] = df['Date'].dt.to_period('M').dt.to_timestamp()
