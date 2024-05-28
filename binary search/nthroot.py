import math
n=27
m=3
l,r=1,n
while l<=r:
    mid=(l+r)//2
    c=mid**m
    if (c)==n:
        print(mid)
        break
    if c>n:
        r=mid-1
    else:
        l=mid+1
    