a=[1,2,4,4,4,5,6,6]
l,r=0,len(a)-1
n=4
res=-1
while l<=r:
    mid=(l+r) //2
    if a[mid]==n:
        res=mid
        l = mid+1
    elif a[mid]<n:
        l=mid+1
    elif a[mid]>n:
        r=mid-1
print(res)
