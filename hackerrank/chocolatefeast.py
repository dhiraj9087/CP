for i in range((int(input()))):
    n,c,m=map(int,input().split())
    a=n//c
    b=a
    #print(a)
    while(b>=m):
        t=b//m
        a=a+t
        b=b-(t*m)+t
    
    print(a)