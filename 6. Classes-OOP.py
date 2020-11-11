class abc:
    def work(self):
        print("its working")
com=abc()
com.work()
print()
######      __init__ method       ######

class A:
    def __init__(self,a):
        self.a=a
        print(a,"working init")
com=A('checkin...')
print()
######      Comparing       ######

class B:
    def __init__(self):
        self.age=20
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False
c1=B()
c1.age=22
c2=B()
if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
print()
######      Types of Methods        ######

class ABC:
    degree= "abcd"
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def avg(self):      #Instance Method
        print("average is: ",(self.m1+self.m2)/2)
    @classmethod
    def uni_name(cls):
        print("university name is: ",cls.degree)
    @staticmethod
    def info():
        print("This is info page")
s=ABC(22,44)
s.avg()
ABC.uni_name()
ABC.info()
s.uni_name()
s.info()
print()
######      Inner Class     ######

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.lap=self.laptop()
    def show(self):
        print(self.name,self.age)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
        def show(self):
            print(self.brand,self.cpu)
st=student("abc",23)
st.show()
lap1=st.laptop()
lap1.show()
print()
######      Inheritence     ######

class A1:
    def A(self):
        print("In A1")
class B1(A1):     #Inheriting A
    def B(self):
        print("In B1")
class C1(B1):        #Multi-level Inheritence
    def C(self):
        print("In C")
class D1(B,C1):        #Multiple Inheritence
    def D(self):
        print("In D")
a=A1()
b=B1()
c=C1()
d=D1()
a.A()
c.A()
print(d.age)
print()
######      Constructor in inheritence      ######

class Cons:
    def __init__(self):
        print("In Constructor")
class In:
    def __init__(self):
        print("In 2nd class")
class Inherit(Cons,In):
    def __init__(self):
        print("Inheriting classes")
        super().__init__()      #Method Resoltuion Order, Left to right
Call=Inherit()
print()