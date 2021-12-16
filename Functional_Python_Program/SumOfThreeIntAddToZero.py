'''
Author: Rakesh Musale
Date: 2022-16-12 10:24:09
Last Modified by: Rakesh Musale
Last Modified time: 2022-16-12 10:24:12
Title : Sum of Three Integer Number Adding to Zero.
'''


print('Enter number of elements : ')
global num
try:
    num=int(input())
except ValueError:
    print("Please enter Integer Value")
    arr=[]
    count=0
    s=0
    print("Enter the elements")
for a in range(num):
    a=int(input())
    arr.append(a)
for i in range(len(arr)):
    for j in range(1,len(arr)):
        for k in range(2,len(arr)):
            s=(arr[i]+arr[j]+arr[k])
            if s==0:
                count+=1
                print(arr[i],arr[j],arr[k])
print(count,"triplet exists")