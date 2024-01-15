nums = [1,2,3,4,5,6,7]
k = 3
n=len(nums)
a=[] 
for i in range(n-k,n):
    a.append(nums[i])
nums=a+nums
for i in range(n-k,n):
    nums.pop()
print(nums)