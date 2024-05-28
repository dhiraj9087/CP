import math
n=25
l,r=1,n
while l<=r:
    mid=(l+r)//2
    c=mid*mid
    if (c)==n:
        print(mid)
        break
    if c>n:
        r=mid-1
    else:
        l=mid+1
    