for i in range((int(input()))):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    p=0
    ab=0
    for i in range(len(a)):
        if(a[i]<=0):
            p+=1
        else:
            ab+=1
    if(p>=k):
        print("NO")
    else:
        print("YES")