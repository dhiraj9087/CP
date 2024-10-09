# def fun(ind,W,dp):
#             if ind==0:
#                return ( W//wt[0])*val[0]
#             if dp[ind][W]!=-1:
#                 return dp[ind][W]
#             nottake = 0 + fun(ind-1,W,dp)
#             take = float('-inf')
#             if W>=wt[ind]:
#                 take = val[ind] + fun(ind,W-wt[ind],dp)
#             dp[ind][W]=max(nottake,take)
#             return dp[ind][W]
#         dp=[[-1]*(W+1) for _ in range(N)]
#         return fun(N-1,W,dp)





for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    w=int(input())
    dp = [[0]*(w+1) for  _ in range(n)]

    for i in range(a[0],w+1):
        dp[0][i] = b[0]
    for i in range(1,n):
        for j in range(1,w+1):
            nottake = 0 + dp[i-1][j]
            take = float('-inf')
            if j>=a[i]:
                take = b[i] + dp[i-1][j-a[i]]
            dp[i][j] = max(take + nottake)
    print(dp[n][w]) 