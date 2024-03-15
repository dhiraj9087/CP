# coins = [1,2,3]
# amount=7
coins=[1,2,5]
amount=11 
n=len(coins)
dp=[[1e9 for j in range(amount+1)] for i in range(n)]
for i in range(amount):
    if i%coins[0]==0:
        dp[0][i]=i//coins[0]
    else:
        dp[0][i]=1e9
for i in range(1,n):
    for j in range(1,amount+1):
        nottake = 0 + dp[i-1][j]
        take = 1e9
        if coins[i]<=amount:
            take = 1 + dp[i][j-coins[i]]
        dp[i][j]=min(take,nottake)
print(dp[n-1][amount])




# def coin(ind,m):
#     if ind==0:
#         if m%coins[0]==0:
#             return m//coins[0]
#         else:
#             return 1e9
#     if dp[ind][m]!=-1:
#         return dp[ind][m]
#     nottake = 0+coin(ind-1,m)
#     take = 1e9
#     if coins[ind]<=m:
#         take=1+coin(ind,m-coins[ind])
#     dp[ind][m]=min(take,nottake)
#     return dp[ind][m]
# print(coin(n-1,amount))