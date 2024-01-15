s,e,d=map(int,input().split())
a=[]
rev=[]
c=0
for i in range(s,e+1):
    a.append(i)
#print(a)
for i in range(len(a)):
    n=str(a[i])
    s=n[len(n)::-1]
    rev.append(int(s))
#print(rev)
for i in range(len(a)):
    if(abs(a[i]-rev[i])%d==0):
        c+=1
print(c)

