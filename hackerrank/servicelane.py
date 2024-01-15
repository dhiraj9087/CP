n,t=map(int,input().split())
width=list(map(int,input().split()))
#print(width)

for i in range(t):
    q=[]
    a,b=map(int,input().split())
    for j in range((b-a)+1):
        q.append((width[a+j]))
    #print(q)
    #continue
    print(min(q))
    