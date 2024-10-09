class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        c=0
        l=list(s)
        n=len(s)
        def fun(ind1,ind2,dp):
            if ind2<0:
                return 1
            if ind1<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s[ind1]==t[ind2]:
                dp[ind1][ind2] = fun(ind1-1,ind2-1,dp) + fun(ind1-1,ind2,dp)
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2] = fun(ind1-1,ind2,dp)
                return dp[ind1][ind2]
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1

        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]
    