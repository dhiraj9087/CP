dp=[-1]*(38)
dp[0],dp[1],dp[2]=0,1,1
def fib(n):
    if dp[n]!=-1:
        return dp[n]
    if n==0 or n==1:
        return n
    elif n==2:
        return 1
    dp[n]=fib(n-1)+fib(n-2)+fib(n-3)
    return dp[n]
# return fib(n)