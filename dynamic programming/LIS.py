# dp=[-1]*(len(nums)+1)
#         def lis(i):
#             if dp[i]!=-1:
#                 return dp[i]
#             ans=1
#             for j in range(i):
#                 if nums[i]>nums[j]:
#                     ans=max(ans,lis(j)+1)
#             dp[i]=ans
#             return dp[i]
#         res=0
#         for i in range(len(nums)):
#             res=max(res,lis(i))
#         return res
import bisect

def lengthOfLIS(nums):
    tails = []
    
    for num in nums:
        # Find the index where 'num' can replace or extend the LIS
        idx = bisect.bisect_left(tails, num)
        print(idx)
        
        # If idx is equal to the length of tails, it means 'num' is larger than any element in tails
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    
    # The length of 'tails' is the length of the longest increasing subsequence
    return len(tails)
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  # Output should be 4, as the LIS is [2, 3, 7, 101]
