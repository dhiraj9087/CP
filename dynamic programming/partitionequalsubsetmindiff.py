arr=[1,2,3,4]
s=sum(arr)
k=s//2
n=len(arr)
dp=[[False for j in range(k+1)] for i in range(n)]
for i in range(n):
    dp[i][0]=True
if arr[0]<=k:
    dp[0][k]==True
for i in range(1,n):
    for j in range(1,k):
        nottake=dp[i-1][j]
        take=False
        if arr[i]<=j:
            take=dp[i-1][j-arr[i]]
        dp[i][j]=(take or nottake)
for i in range(n):
    for j in range(k+1):
        if dp[i][j]:
            print(j)
# print(dp)
print(dp[n-1][j])
