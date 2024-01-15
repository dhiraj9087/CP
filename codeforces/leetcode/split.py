nums = [7,2,5,10,8]
k = 2
arr,arr2=[],[]
n=len(nums)
add=sum(nums)
add2=0
for i in range(n):
    add2+=nums[i]
    arr.append([add2,add-add2])
    arr2.append(abs(add2-(add-add2)))
ind=0
mini=float('inf')
for i in range(n):
    if arr2[i]<mini:
        mini=arr2[i]
        ind=i
ans=arr[ind]
print(max(ans))
print(arr,arr2,ind)