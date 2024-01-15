arr=[2,3,7,8,10]
tar=11
dp = [[False for _ in range(tar+1)] for _ in range(len(arr)+1)]
for i in range(len(arr)+1):
    for j in range(tar+1):
        if i==0:
            dp[i][j]=False
        if j==0:
            dp[i][j]=True
print(dp)