n,a,b=map(int,input().split())
c=0
for i in range(a+1,n+1):
    if n-i<=b:
        c+=1
print(c)
