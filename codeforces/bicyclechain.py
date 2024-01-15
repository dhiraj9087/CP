n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
q,c=[],[]
for i in range(n):
    for j in range(m):
        q.append(b[j]/a[i])
#print(q)
for i in range(len(q)):
    if q[i]-int(q[i])==0:
        c.append(q[i])

print(c.count(max(c)))