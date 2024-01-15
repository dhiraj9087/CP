a=[11,12,15,18,2,4,5,6]
l,r=0,len(a)-1
n=len(a)
while l<=r:
    mid = (l+r)//2
    next = (mid + 1)%n
    prev = (mid+n-1)%n
    if a[mid]<=a[prev] and a[mid]<=a[next]:
        # print(mid,prev,next)
        break
    if a[l]<=a[mid]:
        l=a[mid+1]
    elif a[mid]<=a[r]:
        r=mid-1
print(mid)
