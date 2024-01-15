n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
# print(a)
q=max(a)-min(a)
for i in range(len(a)-n+1):
    q=min(q,a[n-1+i]-a[i])
print(q)