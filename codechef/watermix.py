# cook your dish here
y=int(input())
for i in range(y):
    a,b,x,y=map(int,input().split())
    if(a<b):
        c=(b-a)
        if(c<=x):
            print("YES")
        else:
            print("NO")
    elif(a>b):
        d=(a-b)
        if(d<=y):
            print("YES")
        else:
            print("NO")
    elif(a==b):
        print("YES")