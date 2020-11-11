######      Abstract Class and Abstract Method      ######

from abc import ABC,abstractclassmethod
class computer(ABC):
    @abstractclassmethod
    def process(cls):
        pass
class laptop(computer):
    def process(self):
        print("its running")
class programming:
    def work(self,com):
        print("its working...")
        com.process()

lap=laptop()
lap.process()
prog=programming()
prog.work(lap)
print()
######      Generators      ######

def TopTen():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
values=TopTen()
print(next(values))
for i in values:
    print(i)
print()
######      Exception Handling      ######

a=5
b=2
try:
    print("resource opened")
    print(a/b)
except ZeroDivisionError as e:
    print("You cannot divide a number by zero, ", e)
except ValueError as e:
    print("Invalid Input, ", e)
except Exception as e:
    print("something went wrong, ", e)
finally:
    print("resource closed")
print()
######      Multithreading      ######
'''
from threading import *
from time import sleep
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)
T1=Hello()
T2=Hi()
T1.start()
sleep(.2)
T2.start()
T1.join()
T2.join()
print("bye")
print()'''
######      File Handling       ######

f=open('abc','a')
f.write('\nwriting lines to check more')
f1=open('abc','r')
print(f1.read())
f1=open('abc','r')
f2=open('copy','w')
for i in f1:
    f2.write(i)