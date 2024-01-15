for _ in range((int(input()))):
    n,k=map(int,input().split())
    l,r=[],[]
    for i in range(n):
        l1,l2=map(int,input().split())
        l.append(l1)
        r.append(l2)
    print(l,r)
    