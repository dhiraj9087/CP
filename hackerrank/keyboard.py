

for i in range((int(input()))):
    n,m,c=map(int,input().split())
    q=[]
    for i in range(1,int(c/2)+1):
        if c%i ==0:
            
                q.append([i,int(c/i)])
    #print(q)
    c=0
    for i in range(len(q)):
         if(q[i][0]<=n and q[i][1]<=m):
              c+=1
    print(c)
    

