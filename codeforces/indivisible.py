for i in range((int(input()))):
    n=int(input())
    a=[i for i in range(1,n+1)]
    # print(a)
    # for i in range
    if n==1:
        print(1)
    elif n%2!=0:
        print(-1)
    else:
        q=[i for i in range(1,n+1)]
        od=[i for i in q if i%2!=0]
        ev=[i for i in q if i%2==0]
        # print(od,ev)
        ans=[]
        for i in range(len(od)):
            ans.append(ev[i])
            ans.append(od[i])
        print(*ans)