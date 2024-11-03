from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[ -1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        def fun(ind,buy,cap):
            if ind==n:
                return 0
            if cap==0:
                return 0
            if dp[ind][buy][cap] !=-1:
                return dp[ind][buy][cap]
            if buy:
                dp[ind][buy][cap] = max(-prices[ind]+fun(ind+1,0,cap) , 0 + fun(ind+1,1,cap))
            else:
                dp[ind][buy][cap] = max(prices[ind]+fun(ind+1,1,cap-1), 0 +fun(ind+1,0,cap))
            return dp[ind][buy][cap]
        return fun(0,1,2)