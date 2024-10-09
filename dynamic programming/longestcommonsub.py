class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def fun(ind1,ind2,dp):
            if ind1<0 or ind2<0:
                return 0
            # if ind1==0 and ind2==0:
            #     if text1[ind1]==text2[ind2]:
            #         return 1

            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if text1[ind1]==text2[ind2]:
                dp[ind1][ind2] = 1 + fun(ind1-1,ind2-1,dp)
                return dp[ind1][ind2]
            dp[ind1][ind2] = 0 + max(fun(ind1-1,ind2,dp),fun(ind1,ind2-1,dp))
            return dp[ind1][ind2]
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]


        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[len(text1)][len(text2)]
        # return fun(len(text1)-1,len(text2)-1,dp)
