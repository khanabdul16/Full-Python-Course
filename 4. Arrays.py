from array import *
abc=array('i',[2,3,4,5,6])
print(abc.buffer_info()) #For address and size
abc.reverse() #for reversing the array
print(abc)
for i in abc:  #for print index by index
    print(i)
for i in range(len(abc)):
    print(abc[i])
print()
######      Copying array       ######

copy= array(abc.typecode,(i for i in abc))
print(copy)
print(copy.buffer_info())
print()
######      Inserting and Searching     ######

array=array('i',[])
n=int(input("enter the size: "))
for i in range(n):
    x=int(input("enter the value: "))
    array.append(x)
print(array)
no=int(input("search the no: "))
for i in range(len(array)): #Manual Search
    if array[i]==no:
        print("found at: ")
        break
else:
    print("not found")
print(array.index(no)) #Built-in function for search

from numpy import *
a=array([1,2,3])
b=array([4,5,6,2])
print(concatenate([a,b]))
print()
######      Copying     ######

c=a #address will be same
print(c)
c=a.view() #different address but change in will be change in c too bcaz its a shadow copy
print(c)
c=b.copy()
print(c) #deep copy.
print()
######      Matrix      ######

array=array([[1,2,3],[4,5,6],[7,8,9]])
print(array)
print(array.dtype)  #to know the datatype
print(array.ndim)   #to know the dimension
print(array.shape)  #to know the shape
array1=array.flatten() #to change into single dimension
print(array1)
array2=array1.reshape(3,3) #to convert 1d into 2d
print(array2)
print()

#Matrix

m1=matrix(array) #array to matrix
m2=matrix('1 2 3;4 7 8;3 7 9') #manually adding
print(m2)
print(diagonal(m2)) #to know the diagonal elements
print(m1.min())  #to know the min
m3=m1+m2
print(m3)
print()
m3=m1*m2
print(m3)