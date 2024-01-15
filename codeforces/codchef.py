# cook your dish here
for i in range((int(input()))):
    n,x=map(int,input().split())
    if(n+1<abs(x)):
        print("-1")
    elif(x==1):
         print(n*"*")
    elif(n+1==x):
            print("+++")
    else:
        # c=n-x
        print((x-1)*"+"+(n-(x-1))*"*")
        # print((c-1)*"+" +(n-c-1)*"*" )

