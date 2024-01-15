for _ in range(int(input())):
    dig=int(input())
    lst=list(map(int,input().split()))
    a=set(lst)
    p=0
    for i in a:
        if lst.count(i)%2!=0:
            p=1
    if p==1:
        print("no")
    else:
        print("yes")