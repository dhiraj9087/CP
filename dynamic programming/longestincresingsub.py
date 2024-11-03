from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[[-1]*(n+1) for _ in range(n+1)]

        # def fun(ind,prev):
        #     if ind==n:
        #         return 0
        #     if dp[ind][prev+1]!=-1:
        #         return dp[ind][prev+1]
        #     nottake = 0+fun(ind+1,prev)
        #     take = 0
        #     if prev == -1 or nums[ind]>nums[prev]:
        #         take = 1 + fun(ind+1,ind)
        #     dp[ind][prev+1] = max(take,nottake)
        #     return dp[ind][prev+1]
        # return fun(0,-1)
    

        for i in range(n-1,-1,-1):
                for j in range(i-1,-2,-1):
                    nottake = dp[i+1][j+1]
                    take = 0
                    if j ==-1 or nums[i]>nums[j]:
                        take = 1 + dp[i+1][i+1]
                    dp[i][j+1] = max(take,nottake)
        print(dp)
        return dp[0][0]