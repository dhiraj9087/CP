k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())
a=[]
b=[k,l,m,n,d]
for i in range(1,d+1):
    if i%k!=0 and i%l!=0 and i%m!=0 and i%n!=0:
        a.append(i)
if k==1 or l==1 or m==1 or n==1 :
    print(d)
else:
    print(d-len(a))
