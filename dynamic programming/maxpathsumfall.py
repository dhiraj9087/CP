grid=[[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
grid=[[10, 2, 3], [3, 7, 2], [8, 1, 5]]
n,m=len(grid),len(grid[0])
dp=[[-1 for j in range(m+1)] for i in range(n+1)]
# def fun(i,j):
#     if j<0 or j>=m:
#         return -1e9
#     if i==0 :
#         return grid[0][j]
#     if dp[i][j]!=-1:
#         return dp[i][j]
    # s=grid[i][j]+fun(i-1,j)
    # ld=grid[i][j]+fun(i-1,j-1)
    # rd=grid[i][j]+fun(i-1,j+1)
    # dp[i][j]=max(s,max(ld,rd))
#     return dp[i][j]
# ans=0
# for i in range(1,m+1):
#     ans=max(ans,fun(n-1,m-i))
for i in range(m):
    dp[0][i]=grid[0][i]
for i in range(1,n):
    for j in range(m):
        s=grid[i][j]+dp[i-1][j]
        ld=grid[i][j]
        if j-1>=0:
            ld+=dp[i-1][j-1]
        else:
            ld+=(-1e9)
        rd=grid[i][j]
        if j+1<m:
            rd+=dp[i-1][j+1]
        else:
            rd+=(-1e9)
        dp[i][j]=max(s,max(ld,rd))
print(dp)
ans=dp[n-1][0]
for i in range(1,m):
    ans=max(ans,dp[n-1][i])
print(ans)
# print(fun(n-1,m-1),ans)