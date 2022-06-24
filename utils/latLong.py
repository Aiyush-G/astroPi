import numpy as np 
import pandas as pd
fname = 'MOD_NDVI_M_2020-12-01_rgb_3600x1800.SS.CSV'

#longitude = np.genfromtxt(fname, delimiter=',',usecols=0)

longitude = pd.read_csv(fname, sep=',', usecols=['lat/lon'], squeeze=True)
longitude = list(longitude)
latitude =  pd.read_csv(fname, sep=',', nrows=0, squeeze=True)
latitude = list(latitude.columns.values)
latitude.pop(0)

print(latitude[0])
print(list(longitude))