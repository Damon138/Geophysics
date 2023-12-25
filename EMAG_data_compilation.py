'''
YOU CAN COMPILE MAGNETIC DATA FOR YOUR DESIRED REGION BY ENTERING ITS COORDINATES
FROM EMAG2 CSV FILE WHICH IS AVAILABLE AND CAN BE DOWNLOADED FROM NOAA WEBSITE.
HERE IS THE LINK TO IT:
https://www.ncei.noaa.gov/products/earth-magnetic-model-anomaly-grid-2

Make sure that the script is in same directory as EMAG file.
The whole process of compilation will take some time (around 15 to 20 minutes depending on your computational resources).
In the end you wiil get a csv file containing data for your target region in the same directory named as 'Magnetic_Data.csv'.
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

print('ENTER COORDINATES OF YOUR TARGET REGION  (In Degrees)')
long_min=float(input('Enter minimum Longitude = '))
long_max=float(input('Enter maximum Longitude = '))
lat_min=float(input('Enter minimum Latitude = '))
lat_max=float(input('Enter maximum Latitude = '))

start_time = time.time()

x=pd.read_csv('EMAG2_V3_20170530.csv',chunksize=1000)
df = pd.concat(x)
k=df[(df.iloc[:,3]>lat_min)&(df.iloc[:,3]<lat_max)&(df.iloc[:,2]>long_min)&(df.iloc[:,2]<long_max)]
k.reset_index(inplace=True)
data=pd.DataFrame()
data['LON']=k.iloc[:,3]
data['LAT']=k.iloc[:,4]
data['MAG']=k.iloc[:,6]

data.to_csv('Magnetic_Data.csv')
end_time = time.time()
print("Execution time:", end_time - start_time,' seconds')
