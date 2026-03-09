#1 Len()-Num of elements
from array import array
arr=array('i',[10,20,30,40,50])
print(len(arr))

#2 Append (x)-Add element at end 
from array import array
arr=array('i',[10,20,30,40])
arr.append(50)
print(arr)

#3 Insert(pos,x)-insert at position
from array import array
arr=array('i',[10,30,40])
arr.insert(1,20)
print(arr)

#4 Remove(x)-Remove first occurrence
from array import array
arr=array('i',[10,20,30,40,20,50])
arr.remove(20)
print(arr)

#5 Pop()-Remove and Return last element
from array import array
arr=array('i',[10,20,30,40,50])
x=arr.pop()
print("Removed",x)
print(arr)

#6 Index(x)-Find index of element
from array import array
arr=array('i',[10,20,30,40,50])
print(arr.index(50))

#7 count(x)-count occurrence
from array import array
arr=array('i',[10,20,30,40,50,20])
print(arr.count(20))

#8 Reverse()-Reverse array
from array import array
arr=array('i',[10,20,30,40,50])
arr.reverse()
print(arr)