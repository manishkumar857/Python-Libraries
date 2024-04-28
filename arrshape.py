import numpy as np
arr = np.array([[3,4,5,6],[4,6,5,6]])

#dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr2= np.array([1,2,3,4],ndmin=5)
print(arr.shape)
print(arr2.shape)