# def fun(n,a,k,dp):
#     if n<=0:
#         return 0
#     steps=float('inf')
#     for i in range(1,k+1):
#         if n-i>=0:
#             mini=fun(n-i,a,k,dp)+abs(a[n]-a[n-i])
#             steps=min(steps,mini)
#         else:
#             break
#     return steps
n=10
k=4
a=[40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
dp=[-1]*(n+1)
# print(fun(n-1,a,k,dp))
dp[0]=0
for i in range(1,n):
    ministeps=float('inf')
    for j in range(1,k+1):
        if i-j>=0:
            jump=dp[i-j]+abs(a[i]-a[i-j])
            ministeps=min(ministeps,jump)
    dp[i]=ministeps
print(dp[n-1])
