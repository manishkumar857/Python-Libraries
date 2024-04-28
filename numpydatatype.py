import numpy as np
arr=np.array([1.1,2.1,3.1,4.1,5.5])
arr2=np.array(['apple','mango'])
arr3= np.array([1, 2, 3, 4], dtype='S')

print(arr.dtype)
print(arr2.dtype)
print(arr3.dtype)

#For i, u, f, S and U we can define size as well.
arr4=np.array([1,2,3,4],dtype='i4')
print(arr4.dtype)

#converting datatype
newarr= arr.astype('i')
print(newarr.dtype)

newarr2  =arr.astype('bool')
print(newarr2.dtype)
