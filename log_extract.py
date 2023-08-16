import numpy as np
import pandas as pd

# create file name
wh = input('WH Brand: ')
vol = input('WH Volume: ')
mode = input('DR Mode: ')

data = wh+vol+'_'+mode

# importing csv file
df = pd.read_csv(data+'_Log.csv', header=None)
df = df.dropna(thresh=2) # drops lines with '0'
error_bad_lines=False

# extract time data and converts to datetime
df.insert(1, 'Time', pd.to_datetime(df[0]))
df['Time'] = df['Time'].dt.strftime('%H:%M:%S')
       
# delete original timestamp data
df.drop([0], axis=1, inplace=True)

# convert to numpy array

wd = np.array(df)

# create axis variables
Time = wd[:,0]
EnergyTake = wd[:,-4]
Current = wd[:,-2]/240 # current = power_column/voltage