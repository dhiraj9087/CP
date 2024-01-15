nums = [1,3,4,1,2,3,1]
if len(nums)==len(set(nums)):
    print(nums)
    # return [nums]
d={}
rng=0
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
    rng=max(rng,d[i])
a=[]
# ans=[[] for i in range(rng)]
for i in range(rng):
    ans=[]
    for j,k in d.items():
        if k!=0:
            d[j]-=1
            ans.append(j)
    a.append(ans)
print(a)
