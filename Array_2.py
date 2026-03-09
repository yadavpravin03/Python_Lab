#1 Positive Indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

#2 Negative Indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-2])
print(arr[-4])

#3 Modifying element using index
from array import array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

#4 Index error
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[5])
   #output : IndexError: array index out of range