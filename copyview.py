import numpy as pm
arr=pm.array([5,6,7,8,9])
x=arr.copy()
arr[0]=90

print(x)
print(arr)

#view
y=arr.view()
arr[0]=67
print(y)
print(arr)

#change in view make changes in original array
y[0]=95
print(arr)
print(y)

#check if an array owns it's data or not:

print(x.base)
print(y.base)