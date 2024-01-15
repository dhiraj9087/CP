n,x=map(int,input().split())
a=list(map(int,input().split()))
c=0
q=set(a)
for i in range(n):
    if (x+a[i]) in q:
        # print("Yes")
        c=1
        break
if c==1:
    print("Yes")
else:
    print("No")
