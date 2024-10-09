class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s = word1
        t = word2
        # def fun(i,j):
        #     if i<0:
        #         return j+1
        #     if j<0:
        #         return i+1
        #     if s[i]==t[j]:
        #         return 0+fun(i-1,j-1)
        #     else:
        #         return 1+min(fun(i-1,j-1),fun(i-1,j),fun(i,j-1))
        if s=="" and t=="":
            return 0
        if s==t:
            return 0
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]

        for i in range(len(s)+1):
            dp[i][0] = i
        for i in range(len(t)+1):
            dp[0][i] = i
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = 0 + dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

        return dp[len(s)][len(t)]