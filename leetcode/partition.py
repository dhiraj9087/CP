nums = [1,3,2,4]
# nums = [100,1,10]
nums=[59,51,1,98,73]
nums.sort()
print(nums)
n=len(nums)
d=[]
mini=float('inf')
for i in range(1,n):
    # d[nums[i]-nums[i-1]]=i
    d.append([nums[i]-nums[i-1],i])
    if nums[i]-nums[i-1]<mini:
        mini=nums[i]-nums[i-1]
        ind=i
for i,j in d:
    if j==ind:
        print(i)
        break
# print(d,ind)