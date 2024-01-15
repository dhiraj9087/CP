for i in range((int(input()))):
    n=int(input())
    a=input()
    b=input()
    d1,d2={},{}
    q=[0]
    for i in a:
        if i in d1:
            d1[i]+=1
        else:
            d1[i]=1
    for i in b:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    # print(d1,d2)
    for i in d1:
        if i in d2:
            q.append(min(d1[i],d2[i]))
    print(max(q))
    