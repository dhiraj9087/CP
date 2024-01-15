for i in range((int(input()))):
    n=int(input())
    # x,y,z=0,0,0
    if n<=2:
        print("0")
    elif n==3:
        print('2')
    elif n==4:
        print('3')
    else:
        if n%2!=0:
            x=(n)-(n+1)//2-1
            y=n-1-x
            z=y+2*x
            print(z)
        else:
            x=n//2 - 2
            y=n-1-x
            z=y+2*x
            print(z)