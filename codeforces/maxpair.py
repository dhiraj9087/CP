nums = [51,71,17,24,42]
# nums.sort()
# print(nums)
a=[]
for num in nums:
    digits = [int(digit) for digit in str(num)]
    a.append(digits)
# print(a)
maxi=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if max(a[i])==max(a[j]):
            maxi=max(maxi,nums[i]+nums[j])
print(maxi)