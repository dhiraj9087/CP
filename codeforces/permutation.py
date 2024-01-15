for i in range((int(input()))):
    n=int(input())
    if n==1: print(1)
    elif n%2!=0: print(-1)
    else:
        a=[n] + list(range(1,n))
        # print(*a)
        od=[i for i in a if i%2!=0]
        ev=[i for i in a if i%2==0]
        # print(od,ev)
        od.reverse()
        ans=[]
        for i in range(n//2):
            ans.append(ev[i])
            ans.append(od[i])
        print(*ans)
        