# def fun(n,dp):
#     if n<=1:
#         return n
#     if dp[n]!=-1:
#         return dp[n]
#     dp[n] = fun(n-1,dp)+fun(n-2,dp)
#     return dp[n]
dp=[-1]*10000
# print(fun(5,dp))
n=5
dp[0]=0
dp[1]=1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
print(dp)
