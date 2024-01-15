
# nums = [1,2,8]
# target = 7
# nums = [1,32,1,2]
# target = 12
# nums = [1,32,1]
# target = 35
nums=[128,1,128,1,64]
target=4
# n=len(nums)
# nums.sort()
# add=0
# ans=sum(nums)
# if ans<target:
#     return -1
# a=nums.pop()
# c=0
# while ans!=target:
#     ans -= (a//2)
#     c+=1
#     a=a//2
# print(c)

# nums.sort(reverse=True)
# # print(nums)
# ans=0
# while True:
#     add=0
#     ind=-1
#     for i in range(len(nums)):
#         if add+nums[i]>target:
#             ind=i
#             continue
#         add+=nums[i]
#     if add==target:
#         print(ans)
#         break
#     else:
#         ele=nums.pop(ind)//2
#         nums.append(ele)
#         nums.append(ele)
#     ans+=1