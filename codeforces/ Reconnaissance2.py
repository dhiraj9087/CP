n=int(input())
a=list(map(int,input().split()))
q=[]

for i in range(len(a)-1):
    q.append(abs(a[i]-a[i+1]))
q.append(abs(a[0]-a[len(a)-1]))
z=q.index(min(q))
if z==n-1:
    print(n,1)
else:
    print(z+1,z+2)
#print(q)