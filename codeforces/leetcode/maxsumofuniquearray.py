nums = [2,6,7,3,1,7]
m = 3
k = 4
# nums = [5,9,9,2,4,5,4]
# m = 1
# k = 3
# nums = [1,2,1,2,1,2,1]
# m = 3
# k = 3
nums=[1,1,2]
m=1
k=1
cnt=0
add=0
ans=0
d={}
for i in range(len(nums)):
    # if nums[i] in d:
    #     d[nums[i]]+=1
    # else:
    #     d[nums[i]]=1
    #     cnt+=1
    d[nums[i]] = d.get(nums[i], 0) + 1
    if d[nums[i]] == 1:
        cnt += 1
    add+=nums[i]
    if i>=k-1:
        if cnt>=m:
            ans=max(add,ans)
        d[nums[i-k+1]]-=1
        if d[nums[i-k+1]]==0:
            cnt-=1
        add-=nums[i-k+1]
    # if i<k-1:
    #     continue
    # if cnt>=m:
    #     ans=max(add,ans)
    # d[nums[i-k+1]]-=1
    # if d[nums[i-k+1]]==0:
    #     cnt-=1
    # add-=nums[i-k+1]
print(ans)

