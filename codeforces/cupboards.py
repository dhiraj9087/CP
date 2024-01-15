n=int(input())
l=[]
r=[]
for i in range(n):
    a,b=map(int,input().split())
    l.append(a)
    r.append(b)
l1=l.count(1)
l0=l.count(0)
r1=r.count(1)
r0=r.count(0)
print(min(l1,l0)+min(r1,r0))


