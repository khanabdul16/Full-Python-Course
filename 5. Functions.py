def fun(x,y):
     print("hello ",x+y)
fun(4,5)
print()
######      Function Arguments      ######

def update(x):
    x=8
    print("x is ",x) #Variables aren't mutable
a=10
update(a)
print("a is ",a)

def update1(list1):
    list1[1]=25
    print(list1) #list are mutable
list1=[2,3,4]
update1(list1)

def sum(a,*b): #to get values in tuple in *b
    c=a
    for i in b: #fetching values in b
        c=c+i
    print(c)
sum(5,6,7,8)
print()
######      Keyworded variable length arguments     ######

def person(name, **data):   #one * gets argument, other gets data
    print(name)
    print(data)
    for i,j in data.items(): #to get values in good format.
        print(i,j)

person('abc',age=18,city='isl')
print()
######      Global vs Local Variabale      ######

a,b=5,6  #Global Variables
def function():
    a=10  #Local variables
    global b   #accessing global variable
    b=9     #changing the global variable value
    globals()['a']=8 #changing the global variable 'a' value without effecting local 'a'
    print("In function Local a: ",a)

function()
print("Global Variables a,b: ", a,b)
print()

######      Passing List To Function        ######

def count(list1):
    odd=0
    even=0
    for i in list1:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
list1=[1,2,3,4,5,6,7,8,9,0]
even,odd=count(list1)
print("even: ",even)
print("odd: ",odd)
print("even:{} and odd:{}".format(even,odd))
print()
######          Fibonacci Series        ######

def fib(n):
    a,b=0,1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(3)
print()
######      doubling series of a 1 and its sum      ######

def double(n):
    a=1
    b=0
    for i in range(n):
        print(a)
        b=b+a
        a=a*2
    print("value of b", b)
double(4)
print()
######      Factorial       ######

def Fact(n):
    f=1
    for i in range(n,1,-1):
       f=f*i
    print(f)
Fact(5)
print()
######      Recursion       ######

def fact1(n):   #Factorial using recursion
    if n==0:
        return 1
    return n*fact1(n-1)
result=fact1(4)
print(result)
print()
######      Lamba Function       ######

f=lambda a:a*a
print(f(2))
print()
######      Filter Map Reduce       ######

from functools import reduce
nums=[2,3,4,5,6,7,8]
evens=list(filter(lambda n:n%2==0,nums))
doubles=list(map(lambda n:n*2,evens))
sum1=reduce(lambda a,b:a+b,doubles)
print(evens,"",doubles,"",sum1)
print()
######      Decorators      ######

def div(a,b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner
div1=smart_div(div)
div1(4,8)