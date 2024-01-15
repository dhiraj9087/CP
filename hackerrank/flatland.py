n,m=map(int,input().split())
l=list(map(int,input().split()))
q=[]
for i in range(n):
        q.append(i)
if(n==m):
    print("0")
elif(n%2==0):
     for i in range(len(l)):
           for j in range(len(q)):
                 min(q[j]-l[i])
        

 