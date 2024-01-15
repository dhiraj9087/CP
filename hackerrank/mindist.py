import math
n=int(input())
a=list(map(int,input().split()))
#q=[]
for i in range(n):
    q=[]
    
    for j in range(i+1,n):
        
        if(a[i]==a[j]):
            q.append(i)
            q.append(j)
            #print((q))
            s=0
            w=[]
            for k in range(len(q)):
                
                s=abs(s-q[k])
            w.append(s)
            w=w+w
            print(w)
            