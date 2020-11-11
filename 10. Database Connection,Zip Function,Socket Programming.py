######      Database Connection     ######

import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="khan", database="khan")
mycursor=mydb.cursor()
mycursor.execute("select * from data1")
result=mycursor.fetchall()
print(result)
for i in result:
    print(i)

print()
######      Zip Function        ######

names=("khan","abdul")
age=(23,25)
zipped=zip(names,age)
for a,b in zipped:
    print(a,b)
print()
######      Socket Progrmming       ######

from socket import *

s=socket()
s.bind(('localhost',9999))
s.listen(2)
print("Waiting for the connections")
while True:
    c, addr= s.accept()
    name=c.recv(1024).decode()
    print("Connected with : ",addr,name)
    c.send(bytes("Welcome to Server",'utf-8'))
    c.send(bytes(name, 'utf-8'))
    c.close()