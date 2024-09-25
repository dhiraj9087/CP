
def fun(ind,ans,target,nums,res):
    if target==0:
        ans.add(tuple((res[:])))
        return
    for i in range(ind,len(nums)):
        if i>ind and nums[i]==nums[i-1]:
            continue
        if nums[i]>target:
            break
        res.append(nums[i])
        fun(i+1,ans,target-nums[i],nums,res)
        res.pop()
nums = [10,1,2,7,6,1,5]
target = 8
nums.sort()
res,ans=[],set()
fun(0,ans,target,nums,res)
ans=list(ans)
print(nums)
print(ans)