import numpy as np 
arr=np.array([1,2,3,4,5])
arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:3])
print(arr[1:])
print(arr[:4])

#Return every other element from index 1 to index 5:
print(arr[1:5:2])

#Return every other element from the entire array:
print(arr[::2])

#slicing in 2d array
print(arr2[1, 1:4])
print(arr2[0:2, 2])
print(arr2[0:2, 1:4])  #in this 0:2 last element is included it means 1,2 not 0.