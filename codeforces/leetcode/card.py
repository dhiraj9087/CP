# from collections import defaultdict
# cards=[3,4,2,3,4,7]
# n=len(cards)
# # if n==len(set(cards)):
# #     return -1

# d = defaultdict(lambda: { 'indices': []})
# ans=float('inf')
# for ind,ele in enumerate(cards):
#     # d[ele]['frequency']+=1
#     ans=min(ans,ind-d[ele]['indices'][-1])
#     d[ele]['indices'].append(ind)
    
# d=dict(d)

# # for i in range(n):
# #     if cards[i] in d:
# #         a=(d[cards[i]]+1,i)
        
# #         # d[cards[i]]+=1
# #         d[cards[i]]=a
# #         # ans.add()
# #     else:
# #         a=[1,i]
# #         d[cards[i]]=a
# # ans=list(ans)
# print(d,ans)
import heapq
import math
nums = [1,10,3,3,3]
k = 3
# nums=[756902131,995414896,95906472,149914376,387433380,848985151]
# k=6
n=len(nums)
nums = [-n for n in nums]
print(nums)
res = 0
heap = heapq.heapify(nums)
print(heap)
for _ in range(k):
    a = heapq.heappop(nums) * -1
    res += a
    heapq.heappush(nums, -math.ceil(a/3))
print(res)
# return res
# if 1==len(set(nums)):
#     return k*nums[0]
# nums.sort(reverse=True)
# print(nums)
# ans=nums[0]
# for i in range(1,k):
#     a=math.ceil(nums[i-1]/3)
#     if a>nums[i]:
#         ans+=a
#         nums[i-1]=math.ceil(nums[i-1]/3)
        
#     else:
#         ans+=nums[i]
#         nums[i]=math.ceil(nums[i]/3)
#     print(nums)
#     # ans+=max(a,nums[i])
#     # print(a,nums[i])
# print(ans)