for i in range((int(input()))):
    a,b,c,d=map(int,input().split())
    x=d-b
    y=a+x-c
    if a+x>=c and b<=d:
        print(x+y)
    else:
        print("-1")




    




