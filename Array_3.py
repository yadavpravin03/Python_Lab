#1 BAsic slice 
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[1:4])
print(arr[:3])
print(arr[2:4])
print(arr[:])

#2 Slicing with step
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[::2])
print(arr[1::2])
print(arr[::3])

#3 Negative slicing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])

#4 Reverse array using slicing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[::-1])

#5 Modifying slice
from array import array
arr=array('i',[10,20,30,40,50])
arr[1:4]=array('i',[25,35,45])
print(arr)