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
#check for missing values
missing_values = df.isnull().sum()
#drop missing values
#df = df.dropna()

#keep only key features
key_vars = [
    'Total Player Load', 'Player Load Per Minute', 'Explosive Efforts', 'Session Total Jump', 'Session Jumps Per Minute', 'Total IMA', 'IMA/Min', 'Position'
]
df = df[key_vars]

