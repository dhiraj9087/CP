def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # Write your code here
    dp=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    i,j=n,m
    ans=[]
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            ans.append(s1[i-1])
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
    return ''.join(reversed(ans))
