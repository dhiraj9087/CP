# 2^n number of subsets
def powerset(nums):
    for i in range(1<<len(nums)):
        l=[]
        for j in range(len(nums)):
            if i & (1<<j):
                l.append(nums[j])
        ans.append(l)


    


nums = [1,2,3]
ans=[]
powerset(nums)
print(ans)