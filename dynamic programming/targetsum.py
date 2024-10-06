from typing import List


class Solution:
    def findTargetSumWays(self, arr: List[int], target: int) -> int:
        def fun(ind,tar,dp):
            # if ind<0:
            #     return 0
            # if tar==0:
            #     return 1
            if ind==0:
                if tar==0 and arr[0]==0:
                    return 2
                if tar==0 or tar==arr[0]:
                    return 1
                return 0
            if dp[ind][tar]!=-1:
                return dp[ind][tar]
            l = fun(ind-1,tar,dp)
            r=0
            if tar>=arr[ind]:
                r = fun(ind-1,tar-arr[ind],dp)
            dp[ind][tar] = l+r
            return dp[ind][tar]
        tar = (sum(arr)-target)//2
        tot = sum(arr)
        if tot-target<0:
            return 0
        if (tot - target) % 2 == 1:
            return 0
        dp=[[-1]*(tar+1) for _ in range(len(arr))]
        return fun(len(arr)-1,tar,dp)