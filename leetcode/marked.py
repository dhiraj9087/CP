nums = [1,2,2,1,2,3,1]
queries = [[1,2],[3,3],[4,2]]
a=sorted(nums)
ans=[0]*(len(queries))
d={i:False for i in nums}
d2={}
for i in range(len(nums)):
    if nums[i] not in d2:
        d2[nums[i]]=[]
    else:
        d2[nums[i]].append(i)
add=[]
s=0
tot=sum(nums)
for i in range(len(nums)):
    s+=a[i]
    add.append(s)
print(queries[0][0])
for i in range(len(queries)):
    if d[nums[queries[i][0]]]==False:
        d[nums[queries[i][0]]]=True
        ans[i]=tot-add[queries[i][1]-1]-nums[queries[i][0]]
    else:
        ans[i]=tot-add[queries[i][1]-1]
print(nums,d,add,ans)
