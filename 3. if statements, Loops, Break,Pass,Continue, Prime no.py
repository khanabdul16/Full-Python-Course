######      If Statement        ######

x=2
y=3
if x<y:
    print("greater")
elif x==y:
    print("equal")
else:
    print("lesser")
print()
######      While Loop      ######

x=1
while x<=5:
    print(x,end=" ")
    x+=1
print()
######      For Loop        ######

x=[1,3,34,4,5]
for i in x:
    print(i,end=" ")
print()
for i in range(2,10,3): #startpoint, endpoint, difference
    print(i,end=" ")
print()
######      Break,Pass, Continue        ######

x=6
for i in range(0,x,1):
    if i>4:
        break
    print(i,end="")
print()
for i in range(0, x, 1):
   pass
print()
for i in range(0, x, 1):
    if i %2== 1:
        continue
    print(i,end="")
print()
######      Prime Or Not        ######

num=9
for i in range(2,num):
    if num%i==0:
        print("not prime and divisible by ",i)
        break
else:
    print("prime")
