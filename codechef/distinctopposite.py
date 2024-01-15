for i in range((int(input()))):
    a=int(input())
    q=[]
    for i in range(1,(a)//2 + 1):
        q.append(i)
    #print(q)
    for i in range(a,a//2,-1):
        q.append(i)
    #print(q)
    print(' '.join(map(str,q)))


