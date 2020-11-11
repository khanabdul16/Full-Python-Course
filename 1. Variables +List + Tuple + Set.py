myname = 'khan'
print(myname)
print(len(myname))
print()
######      List        ######

nums=[12,3,4,43,35]
names=['sdsqdfs','dfdf','dfdf']
print(nums,names)
mil=[nums,names]
print(mil)
nums.append(434)
nums.insert(2,45)
nums.remove(4)
nums.pop(3)
print(nums)
del nums[2:4]
nums.extend([23,525,52])
print(nums)
a=min(nums)
print(a)
nums.sort()
print(nums)
print()
######      Tuple       ######

tup=(21,3,44,3) #not mutable, can add or remove or change
print(tup)
print(tup.count(3))
print()
######      Set     ######
set={2,324,5,54,5,665,544}  #no value repeat, no sequence
print(set)


