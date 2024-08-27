def fun(ind,ans,target,nums,res):
        if ind==len(nums):
            if target==0:
                ans.append(res[:])
            return
        if nums[ind]<=target:
            res.append(nums[ind])
            fun(ind,ans,target-nums[ind],nums,res)
            res.pop()
        fun(ind+1,ans,target,nums,res)
nums = [2,3,6,7]
target = 7
res,ans=[],[]
fun(0,ans,target,nums,res)
print(ans) 