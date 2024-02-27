m,n=2,2
# def fun(i,j,dp):
#     if i==0 and j==0:
#         return 1
#     if i<0 or j<0:
#         return 0
#     if dp[i][j]!=-1:
#         return dp[i][j] 
#     l=fun(i-1,j,dp)
#     r=fun(i,j-1,dp)
#     dp[i][j]=l+r
#     return dp[i][j]
dp=[[-1 for j in range(n+1)] for i in range(m+1)]
# print(fun(2,1,dp)) 
# print(dp)
# m,n=2,2

for i in range(m):
    for j in range(n):
        if i==0 and j==0:
            dp[0][0]=1
        else:
            l,r=0,0
            if i>0:
                l=dp[i-1][j]
            if j>0:
                r=dp[i][j-1]
            dp[i][j]=l+r
print(dp)
print(dp[m-1][n-1])

