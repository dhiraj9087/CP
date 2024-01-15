for i in range((int(input()))):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    c=0
    for i in range(n):
        if min(l1[i],l2[i])*2<max(l1[i],l2[i]):
            c+=1
    print(n-c)