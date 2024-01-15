for i in range((int(input()))):
    n,m,k=map(int,input().split())
    lst=map(int,input().split())
    c=0
    for i in lst:
        if i==1:
            c+=1
    
    if(c==n):
        print("100")
    elif(c==m):
        print(k)
    else:
        print("0")