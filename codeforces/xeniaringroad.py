n,m=map(int,input().split())
a=list(map(int,input().split()))
c=a[0]-1
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        c+=n-a[i]+a[i+1]
    elif a[i]<a[i+1]:
        c+=a[i+1]-a[i]
print(c)