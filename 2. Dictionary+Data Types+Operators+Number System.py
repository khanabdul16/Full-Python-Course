######      Dictionary      ######

data={1:"abc",2:"ahgy",3:"hsudyi"}
print(data)
print(data[1])
print(data.get(2))
key=[1,2]
value=["adfdg","adfyd"]
data1=dict(zip(key,value))
print(data1)
print()
#adding in data
data1[3]='sdgyu'
print(data1)
#Del in data
del data1[1]
print(data1)
print()
######      Nested Dictionary       ######

data2={1:'khan',2:['abdul','khan'],3:{'a':'xkgydi', 'b':'gfujhi'}}
print(data2)
print()
######      Data Types      ######

a=5.6
b=int(a) #converting float a into int
print(b)
a=range(0,10) #Range
for i in a:  #Fetching data in Range
    print(i)
print(list(range(10))) #Print list of range
print(data1.keys()) #getting keys in dictionary
print()
######      Number System       ######

x=25
print(bin(x)) #Converting into binary
print(oct(x)) #Converting into Octa
print(hex(x)) #Converting into Hexa
print()
######      Swapping        ######

a,b=5,6
a=a+b
b=a-b
a=a-b
print(a,b)
a,b=b,a #in python swapping
print(a,b)
print()
######      Math Fuctions       ######

import math
y=math.sqrt(10) #for square root
print(y)
print(math.floor(y)) #for lower round
print(math.ceil(y)) #for upper root
print(math.pow(y,2)) #for power
print(math.pi) #for Pi Value
print(math.e) #for e Value

