n,m=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
s,q=0,[]
for i in range(m):
    s+=a[i]
    q.append(-s)
if max(q)<0:
    print('0')
else:
    print(max(q))
#print(a)