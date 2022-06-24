# load numpy array from npz file
# generate CSV files for each pixel with date
from numpy import load
import pandas as pd
import os


# load dict of arrays
dict_data = load('data.npz')
# extract the first array
data = dict_data['arr_0']
# print the array

# (1800, 3600, 253)
#   Y      X    Z
print(data.shape)

# returns dates from filename
dates = []
directory = os.path.abspath(os.path.dirname(__file__))+"/NDVICSV"
for filename in os.listdir(directory):

    if filename.endswith(".CSV"): 
        newDate = str(pd.to_datetime(filename, format="MOD_NDVI_M_%Y-%m.CSV"))
        dates.append(newDate) 

    else:
        continue

print(dates)
'''
    for x in range(0, 3600):
        for y in range(0, 1800):
            for z in range (0,253):
                lst.append([dates[z], data[y][x][z]])
                #print(data[600][1800][z])
'''

# For file names , lat & long
fname = 'MOD_NDVI_M_2020-12-01_rgb_3600x1800.SS.CSV'

#longitude = np.genfromtxt(fname, delimiter=',',usecols=0)

longitude = pd.read_csv(fname, sep=',', usecols=['lat/lon'], squeeze=True)
longitude = list(longitude)
latitude =  pd.read_csv(fname, sep=',', nrows=0, squeeze=True)
latitude = list(latitude.columns.values)
latitude.pop(0)

def generateDatasets(dates, data):
    for x in range(0, 3600):
        print("x at",x)
        for y in range(0, 1800):
            print("y at",y)
            lst = []
            for z in range (0,253):
                lst.append([dates[z], data[y][x][z]])
                #print(data[600][1800][z])

                df = pd.DataFrame(lst, columns =['Date', 'Value'])
                directory = os.path.abspath(os.path.dirname(__file__))+"/datasetsZ"+"/"+str(latitude[x])+","+str(longitude[y])+".csv"
                df.to_csv(directory, encoding='utf-8', index=False)
                

generateDatasets(dates, data)
