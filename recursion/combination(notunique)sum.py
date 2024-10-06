# def fun(ind,ans,target,nums,res):
#         if ind==len(nums):
#             if target==0:
#                 ans.append(res[:])
#             return
#         if nums[ind]<=target:
#             res.append(nums[ind])
#             fun(ind,ans,target-nums[ind],nums,res)
#             res.pop()
#         fun(ind+1,ans,target,nums,res)
def fun(ind ,tar):
    if ind==0:
        if tar%nums[ind]==0:
            return 1
        else:
            return 0
    nottake = fun(ind-1,tar)
    take = 0
    if tar>=nums[ind]:
        take = fun(ind,tar-nums[ind])
    return take + nottake
nums = [2,3,6,7]
target = 7
# nums = [1,2,5]
# target = 5
res,ans=[],[]
print(fun(len(nums)-1,target))
# fun(0,ans,target,nums,res)
print(ans)