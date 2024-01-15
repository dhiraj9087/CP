for i in range((int(input()))):
    n,d=map(int,input().split())
    a=int(input())
    q=str(a)
    f=0
    q = str(a)
    f = False
    for i in range(len(q)):
        if d > int(q[i]):
            print(int(q[:i] + str(d) + q[i:]))
            f = True
            break
    if not f:
        print(int(q + str(d)))
