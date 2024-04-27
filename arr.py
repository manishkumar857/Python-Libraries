import numpy as np
arr =np.array([1,2,3,4,5],ndmin=10) #setting the dimension to 10
arrm = np.array([[1,2,3,4,5], [3,4,5,6,7]])
arr3 = np.array([[[1,2,3,4,5], [3,4,5,6,7], [8,9,9,6,4]]])
print(arr)
print(arrm)
print(arr3)
print(type(arr))
#printing the dimension of array
print(arr.ndim)
print(arrm.ndim)
print(arr3.ndim)