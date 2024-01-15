for i in range((int(input()))):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    q=[] 
    index=[]
    if(min(a)>k):
        print("0")
    else:
        for i in range(n):
            c=a[i]+b[i]
            if(c<k):
                q.append(c)
        s=0
        # print(len(q))
        for i in range(len(q)):
            s+=q[i]
            #print(s)
            if(s<=k):
                index.append(s)
        
        print(index)
        for i in range(len(index)):
            if(a[len(index)+1]+index[0]<=k):
                print(len(index)+1)
            else:
                print(len(index))
        