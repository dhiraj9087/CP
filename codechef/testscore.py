y=int(input())
for y in range(y):
    a,b,c=map(int,input().split())
    if(b>c):
        if(c==0):
            print("YES")
        print("NO")
    elif(b%a==0):
        print("YES")
    else:
        print("NO1")
