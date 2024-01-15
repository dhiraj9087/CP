def solve():
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(n-1):
        if a[i]!=a[i+1]: c+=1
    # print(c)
    C=[0]*n
    for i in range(n):
        if a[i]==0:
            C[i]=1
        else:
            C[i]=0
    print(*C)
    
    


    


for _ in range((int(input()))):
    solve()