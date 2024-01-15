for i in range((int(input()))):
    n=int(input())
    c=list(map(int,input().split()))
    c.sort()
    # print(c)
    flag=False
    if c[0]>1:
        print("NO")
    else:
        var=c[0]
        for i in range(1,n):
            if c[i]<=var:
                var+=c[i]
            else:
                flag=True
                break
        if flag:
            print("NO")
        else:
            print("YES")

    # pre_sum=[]
    # s=0
    # for i in c:
    #     s+=i
    #     pre_sum.append(s)
    # # pre_sum.append(s)
    # print(pre_sum)
    # count=0
    # for i in range(n-1,-1,-1):
    #     # print(c[i],end=' ')
    #     var=c[i]
    #     # for j in range()
    # print()
    # print(count)


