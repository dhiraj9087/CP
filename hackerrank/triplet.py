n,d=map(int,input().split())
a=list(map(int,input().split()))
q=[]
c=0
for i in range(len(a)):
    q=[a[i]]
    s=a[i]
    for j in range(i+1,n):
        if(a[j]==s+d):
            q.append(a[j])
            s=a[j]
            if(len(q)==3):
                c+=1
                break
    # if(len(q)==3)
    # print(q)
print(c)