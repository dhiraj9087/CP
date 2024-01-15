# nums = [1,0,2]
# target = 1
# nums = [1,3,6,4,1,2]
# target = 3
nums = [1,3,6,4,1,2]
target = 0

n=len(nums)
c=0
# l,r=0,1
# ind=0
# while r<n:
#     if abs(nums[l]-nums[r]) <= target:
#         c+=1
#         ind=r
#         l=r
#         r+=1
        
#     else:
#         r+=1
# if ind!=n-1:
#     print(-1)
# else:
#     print(c)
l,r=n-2,n-1
ind=0
while r>0:
    if abs(nums[l]-nums[r]) <= target:
        c+=1
        ind=l
        r=l
        l-=1
    else:
        l-=1
if ind!=0:
    print(-1)
else:
    print(c)
