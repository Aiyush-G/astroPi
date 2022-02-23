import os
from numpy import genfromtxt, dstack, savez_compressed

directory = os.path.abspath(os.path.dirname(__file__))+"/NDVICSV"
arr3d1 = directory + "/MOD_NDVI_M_2000-03.CSV"
arr3d2 = directory + "/MOD_NDVI_M_2000-04.CSV"
arr3d3 = directory + "/MOD_NDVI_M_2000-05.CSV"

"""
arr1 = genfromtxt(arr3d1, delimiter=',')
arr2= genfromtxt(arr3d2, delimiter=',')
arr4= genfromtxt(arr3d3, delimiter=',')

arr3 = array([arr1, arr2])
print (arr3.shape)

arr3 = dstack((arr3, arr4))
print (arr3.shape)
"""


# numpy.dstack((A, B)).shape

#arr1 = genfromtxt(arr3d1, delimiter=',')
#arr2= genfromtxt(arr3d2, delimiter=',')

#arr3dMAIN = array([arr3d1, arr3d2])
#print (arr3dMAIN.shape)

allArrays = []

for filename in os.listdir(directory):
    if filename.endswith(".CSV") or filename.endswith(".py"): 
         #print(filename)
         dirFile = directory + "/" + filename
         arr = genfromtxt(dirFile, delimiter=',')
         print(arr.shape, dirFile)
         allArrays.append(arr)
        
    else:
        continue


arr3dMain = newarray = dstack(allArrays)
savez_compressed("data.npz", arr3dMain)
# print(arr3dMain)
print(arr3dMain.shape)