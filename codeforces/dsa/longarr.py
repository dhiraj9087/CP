a=[8,4,3,1,5,9,2]
k=2
n=len(a)
a_pre=[]
s=0
for i in range(n):
    s+=a[i]
    a_pre.append(s)
print(a_pre)
for i in range(n-1,-1,-1):
    if a_pre[i]%2!=0:
        print(a_pre[i])
        break