for i in range((int(input()))):
    a,b,c=map(int,input().split())
    if(a==b==c):
        print("0")
    elif(a!=b and b!=c and c!=a):
        print("-1")
    else:
        if(abs(max(a,b)-c)>1 and abs(max(a,b)-c)%2==0):
            #if(abs(max(a,b)-c)%2==0):
                print(abs(max(a,b)-c)//2)
        else:
            print("-1")

    #print(abs(max(a,b)-c)//2)