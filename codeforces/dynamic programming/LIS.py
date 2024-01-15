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