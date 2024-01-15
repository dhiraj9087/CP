for i in range((int(input()))):
    n,m=map(int,input().split())
    if n==1 or m==1:
        print("1")
        print(n,m)
    else:
        print("2")
        print("1",m-1)
        print(n,m)