class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        dp=[[0]*(m+1) for _ in range(n+1)]
        # for i in range(n + 1):
        #     dp[i][0] = 0
        # for i in range(m + 1):
        #     dp[0][i] = 0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        i,j=n,m
        sub=""
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                sub+=str1[i-1]
                i-=1
                j-=1
            elif dp[i-1][j] > dp[i][j-1]:
                sub+=str1[i-1]
                i-=1
            else:
                sub+=str2[j-1]
                j-=1
        while i>0:
            sub+=str1[i-1]
            i-=1
        while j>0:
            sub+=str2[j-1]
            j-=1

        sub = sub[::-1]
        # print(sub,str1.index(sub),str2.index(sub))
        # ind1,ind2 = str1.index(sub),str2.index(sub)
        # ans=sub
        # if ind2>ind1:
        #     ans = str2[:ind2] + sub + str2[ind2+len(sub)-1:] + 

        return sub