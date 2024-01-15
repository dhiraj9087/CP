for i in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    z=[]
    if len(set(a))==len(a):
        print(n-1)
    else:
        for i in set(a):
            z.append(a.count(i))
        print(n-max(z))
