for _ in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    q=abs(a[0]-a[1])
    for i in range(1,n-1):
        m=max(abs(a[i] - a[i - 1]), abs(a[i] - a[i + 1]))
        q=min(m,q)
    q=min(q,abs(a[n-2]-a[n-1]))
    print(q)




