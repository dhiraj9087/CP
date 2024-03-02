# grid = [[1,2,3],[4,5,6]]
grid=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]

n,m=len(grid),len(grid)
dp=[[-1 for j in range(n+1)] for i in range(n+1)]
# def fun(i,j):
#     if i==n-1:
#         return grid[n-1][j]
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     l=grid[i][j]+fun(i+1,j)
#     r=grid[i][j]+fun(i+1,j+1)
#     dp[i][j]=min(l,r)
#     return dp[i][j]
# print(fun(0,0))
for i in range(n):
    dp[n-1][i]=grid[n-1][i]
for i in range(n-2,-1,-1):
    for j in range(i,-1,-1):
        l=grid[i][j]+dp[i+1][j]
        r=grid[i][j]+dp[i+1][j+1]
        dp[i][j]=min(l,r)
print(dp[0][0])