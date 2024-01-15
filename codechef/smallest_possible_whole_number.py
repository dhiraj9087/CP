y=int(input())
for i in range(y):
    a,b=map(int,input().split())
    if(a<b):
        print(a)
    elif(a==b):
        print("0")
    else:
        for i in range(2):
            c=(a-b)
            if(c>=b):
                d=c-b
                print(d)
            elif(c<b):
                print(c)