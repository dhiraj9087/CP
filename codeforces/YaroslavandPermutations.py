n=int(input())
a=list(map(int,input().split()))
q={}
for i in a:
    q[i]=a.count(i)
z=(max(q.values()))
if n%2==0:
    if z<=n/2:
        print("YES")
    else:
        print("NO")
else:
    if z-1 <= n//2:
        print("YES")
    else:
        print("NO")