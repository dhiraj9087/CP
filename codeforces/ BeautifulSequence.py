for i in range((int(input()))):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    for i in range(n):
        if i+1 in a[i::]:
            flag=1
            # print(i+1)
    if flag==1:
        print("YES")
    else:
        print("NO")
