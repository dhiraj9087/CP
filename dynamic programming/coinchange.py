coins = [1,2,5]
amount=11
# inf=float('inf')
# dp=[inf for i in range(amount+1)]
# dp[0]=0
# for amt in range(amount+1):
#     for i in coins:
#         if i<=amt:
#             dp[amt]=min(dp[amt],dp[amt-i]+1)
# # if 
# print(dp)
dp = [0] * (amount + 1)
dp[0] = 1

for coin in coins:
    for j in range(coin, amount + 1):
        dp[j] += dp[j - coin]

# return dp[amount]
print(dp[amount])