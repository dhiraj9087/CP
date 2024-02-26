n=3
a=[[1,2,5],[3,1,1],[3,3,3]]
# def fun(ind,lastday,dp):
#     if dp[ind][lastday]!=-1:
#         return dp[ind][lastday]
#     if ind==0:
#         maxi=0
#         for i in range(3):
#             if i!=lastday:
#                 maxi=max(maxi,a[0][i])
#         dp[ind][lastday]=maxi
#         return dp[ind][lastday]
#         # return maxi
#         # return max(a[ind])
    
#     maxi=0
#     for i in range(3):
#         if lastday!=i:
#             points=a[ind][i]+fun(ind-1,i,dp)
#             maxi=max(maxi,points)
#     dp[ind][lastday]=maxi
#     return dp[ind][lastday]
dp=[[-1]*(n+1) for _ in range(n+1)]
# print(dp)
# print(fun(2,3,dp))
dp[0][0]=max(a[0][1],a[0][2])
dp[0][1]=max(a[0][0],a[0][2])
dp[0][2]=max(a[0][0],a[0][1])
dp[0][3]=max(a[0][0],a[0][1],a[0][2])
for i in range(1,n):
    for last in range(4):
        dp[i][last]=0
        maxi=0
        for j in range(3):
            if j!=last:
                mark=a[i][j]+dp[i-1][j]
                dp[i][last]=max(dp[i][last],mark)
        
print(dp[n-1][3])