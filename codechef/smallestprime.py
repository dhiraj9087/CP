for i in range((int(input()))):
    x,y=map(int,input().split())
    if(x%2==0):
        if((y-x)%2==0):
            print(((y-x))//2)
        else:
            print(((y-x))//2+1)


    else:
        if(x==7 or x==5):
            x=x+x
            a=y-x
            if(a%2==0):
                print(((a)//2)+1)
            else:
                print(((a)//2)+2)
        else:
            x=x+3
            a=y-x
            if(a%2==0):
                print(((a)//2)+1)
            else:
                print(((a)//2)+2)

    #print(c)
    