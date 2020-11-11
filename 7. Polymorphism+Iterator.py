class PyCharm:
    def execute(self):
        print("compiling...")
class Notepad:
    def execute(self):
        print("debugging...")
        print("compiling...")
class Program:
    def code(self,ide):
        ide.execute()
ide=Notepad()       #it can be PyCharm too. as both have method execute. thats what call duck typing
Prog=Program()
Prog.code(ide)
print()
######      Operator Overloading        ######

class student:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        a=self.a+other.a
        b=self.b+other.b
        s3=student(a,b)
        return s3
    def __gt__(self, other):
        r1=self.a+self.b
        r2=other.a+other.b
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.a,self.b)

s1=student(45,66)
s2=student(55,76)
s3=s1+s2
print(s3.a,s3.b)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
print(s1)
print()
######      Method Overloading      ######

#Python does not support Method Overloading so we achieve it through manual steps
class abc:
    def sum(self,a=0,b=0,c=0):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

r=abc()
print(r.sum(3,4,6))
print(r.sum(4,5))
print()
######      Method Overriding       ######

class A:
    def show(self):
        print("In A")
    def show(self): #Overriding
        print("override")
class B(A):
    def show(self): #Overriding
        print("In B")
a=A()
a.show()
print()
######      Iterator        ######

class TopTen:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()
print(next(values))
for i in values:
    print(i)