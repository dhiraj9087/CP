# nums = [5,10,1,5,2]
# k = 1
# ans=[]
# for i in range(len(nums)):
#     b=format(i,'b')
#     ans.append(b)
# print(ans)
# res=0
# for i in range(len(ans)):
#     c=ans[i].count('1')
#     if c==k:
#         res+=nums[i]
# print(res)
nums = [6,0,3,3,6,7,2,7]
nums.sort()
print(nums)
n=len(nums)
add=[0]*(len(nums)+1)
s=0
ans=0
# for i in range(n):
#     for j in range(i+1,n):
#         if nums[j]==j+1:
#             ans+=1
# print(ans)
# return ways
if nums[0]>0:
    ans+=1
for i in range(n):
    if nums[i]<(i+1) and ((i+1)<n and nums[i+1]>(i+1)):
        ans+=1
    elif nums[i]<i+1 and i+1==n:
        ans+=1
print(ans)

