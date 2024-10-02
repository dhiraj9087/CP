n=3
a=[1,2,4]
# ans=[]
# def fun(ind,dp):
#     if ind==0:
#         return a[ind]
#     if ind<0:
#         return 0
#     if dp[ind]!=-1:
#         return dp[ind]
#     left = a[ind]+fun(ind-2,dp)
#     right=0+fun(ind-1,dp)
#     dp[ind]=max(left,right)
#     return dp[ind]
dp=[-1]*(n+1)
# print(fun(n-1,dp))
dp[0]=a[0]
neg=0
for i in range(1,n):
    if i>1:
        take = a[i]+dp[i-2]
    else:
        take = a[i]
    nottake=dp[i-1]
    dp[i]=max(take,nottake)
print(dp[n-1])

# print(ans)
# dp=[-1]*(n+1)
# # print(fun(n-1,a,k,dp))
# dp[0]=0
# for i in range(1,n):
#     ministeps=float('inf')
#     for j in range(1,n+1):
#         if i-j<:
#             jump=dp[i-j]+abs(a[i]-a[i-j])
#             ministeps=min(ministeps,jump)
#     dp[i]=ministeps
# print(dp[n-1])