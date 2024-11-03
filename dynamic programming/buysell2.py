from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        def fun(ind,buy):
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy==1:
                dp[ind][buy]=max(-prices[ind]+fun(ind+1,0) , 0+ fun(ind+1,1))
            else:
                dp[ind][buy] = max(prices[ind]+fun(ind+1,1) , 0 + fun(ind+1,0))
            return dp[ind][buy]
        dp=[[0]*(2) for _ in range(n+1)]
        dp[n][0]=0
        dp[n][1]=0
        for i in range(n-1,-1,-1):
            for j in range(2):
                if j==1:
                    dp[i][j] = max(-prices[i]+dp[i+1][0],dp[i+1][1])
                else:
                    dp[i][j] = max(prices[i]+dp[i+1][1],dp[i+1][0])

        print(dp)
        return dp[0][1]