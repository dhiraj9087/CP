for i in range((int(input()))):
    a=int(input())
    s=1
    if(a%2==0):
        for i in range(a//2):
            s=s*2
            s=s+1
        print(s)
    else:
        for i in range((a+1)//2):
            s=s*2
            s=s+1
        print(s-1)
    

    