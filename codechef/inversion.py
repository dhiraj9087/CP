for i in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    d=a.sort()
    if a == d:
        print(2**n - 1)
    else:
        q=[]
        for i in range(1,n-1):
            if a[i]>a[i+1]:
                q.append(a[i])
        print(q)