# grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
m,n=len(grid),len(grid[0])
dp=[[-1 for j in range(n+1)] for i in range(m+1)]
# m,n=len(grid),len(grid[0])
# def fun(i,j,dp):
#     if i==0 and j==0:
#         return grid[i][j]
#     if i<0 or j<0:
#         return 10000000
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     l=grid[i][j] +   fun(i-1,j,dp)
#     r=grid[i][j] +   fun(i,j-1,dp)
#     dp[i][j]=min(l,r)
#     return dp[i][j]
# # dp
# print(fun(m-1,n-1,dp))
# print(max(ans))
for i in range(m):
    for j in range(n):
        if i==0 and j==0:
            dp[i][j]=grid[i][j]
        else:
            l,r=grid[i][j],grid[i][j]
            if i>0:
                l+=dp[i-1][j]
            else:
                l+=int(1e9)
            if j>0:
                r+=dp[i][j-1]
            else:
                r+=int(1e9)
            dp[i][j]=min(l,r)
print(dp[m-1][n-1])