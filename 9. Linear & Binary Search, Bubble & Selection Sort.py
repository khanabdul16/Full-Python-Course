######      Linear Search       ######
pos=0
def search(list,n):
    i=0
    for i in range(0, len(list), 1):
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False
list=[3,4,6,7,8,9,44,32]
n=32
if search(list,n):
    print("found at index: ",pos)
else:
    print("not found")
print()
######      Binary Search       ######

ind=0
def search1(list1,n1):
    l=0
    u=len(list1)-1
    while l<=u:
        mid=(l+u)//2
        if list1[mid]==n1:
            globals()['ind']=mid
            return True
        else:
            if list1[mid]<n1:
                l=mid+1
            else:
                u=mid-1
    return False
list1=[3,4,6,7,8,9,32,44]
n1=44
if search1(list1,n1):
    print("found at index: ",ind)
else:
    print("not found")
print()
######      Bubble Sort     ######

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

nums=[23,5,56,67,785,333]
sort(nums)
print(nums)
print()
######      Selection Sort      ######

def sort(nums1):
    for i in range(len(nums1)-1,0,-1):
        max=i
        for j in range(i):
            if nums1[j]>nums1[max]:
                max=j

        temp=nums1[i]
        nums1[i]=nums1[max]
        nums1[max]=temp

nums1=[23,5,56,67,785,333]
sort(nums1)
print(nums1)