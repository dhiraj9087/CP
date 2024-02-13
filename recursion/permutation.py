from collections import defaultdict
def fun(nums,res,ans,n,d):
    if len(res)==n:
        ans.append(res[:])
        return
    for i in range(n):
        if not d[i]:
            d[i]=True
            res.append(nums[i])
            fun(nums,res,ans,n,d)
            res.pop()
            d[i]=False

nums=[1,2,3]
res,ans,d=[],[],defaultdict(bool)
fun(nums,res,ans,len(nums),d)
print(ans)