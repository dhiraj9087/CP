# def fun(n,a):
#     if n<0:
#         return 0
#     left = fun(n-1,a)+abs(a[n]-a[n-1])
#     right=float('inf')
#     if n>1:
#         right = fun(n-2,a)+abs(a[n]-a[n-2])
#     return min(left,right)
a=[10 ,50 ,10]
n=3
# print(fun(n-1,a))
dp=[-1]*(n+1)
dp[0]=0
for i in range(1,n):
    left = dp[i-1]+abs(a[i]-a[i-1])
    right=float('inf')
    if i>1:
        right = dp[i-2]+abs(a[i]-a[i-2])
    dp[i]=min(left,right)
print(dp[n-1])