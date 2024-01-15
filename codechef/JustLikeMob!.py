for _ in range((int(input()))):
    n,m,k,x=map(int,input().split())
    q=[]
    days=0
    for i in range(1,x):
        if i%k==0:
            days += (n+m)
            q.append(days)
        else:
            days += n
    # print(days,q)
    for i in range(len(q)):
        if q[i]>x:
            if q[i]-(n+m) < x :
                print("YES")
                break
    else:
        print("NO")
        