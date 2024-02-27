import math
from collections import *
def printDivisors(n):
    a=[]
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                a.append(i)
            else:
                a.append(i)
                a.append(n//i)
    return a

n=5
arr=[2,3,4,5,6]
n=6
arr=[5,8,7,5,5,4]
n=5
arr=[233, 603, 405, 563, 518]
d=defaultdict(int)
for i in range(n):
    a=printDivisors(arr[i])
    for j in range(len(a)):
        d[a[j]]+=1
del d[1]
maxi=float('-inf')
key=0
for i,j in d.items():
    if j>maxi:
        maxi=j
        key=i
print(d,key)
ans=0
odd=0
for i in range(n):
    if arr[i]%key!=0:
        ans+=key-(arr[i]%key)
    if arr[i]%2!=0:
        odd+=1
print(min(odd,ans))
