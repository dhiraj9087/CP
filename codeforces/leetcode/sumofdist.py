nums = [3,1,6,8]
queries = [1,5]
n,m=len(nums),len(queries)
arr=[]
nums.sort()
#         for i in range(m):
#             for j in range(n):
#                 arr[i] += (abs(nums[j]-queries[i]))
#         return arr
#         for j in range(n):
#             arr[0] += (abs(nums[j]-queries[0]))
#         ans=arr[0]
    
#         for i in range(1,m):
#             # if queries[i]>queries[0]:
#             #     arr[i]=arr[0]-abs(queries[i]-queries[0])
#             # else:
#             #     arr[i]=arr[0]+abs(queries[i]-queries[0])
#             res=abs(queries[i]-queries[i-1])
#             ans+=res*n
#             arr[i]=ans
#         return arr
pre=[0]*(n+1)
for i in range(n):
    pre[i+1]=pre[i]+nums[i]
print(pre)

for i in range(m):
    l,r=0,n
    while l<r:
        mid=l+(r-l)//2
        if nums[mid]>queries[i]:
            r=mid
        else:
            l=mid+1
    a = queries[i]*l - pre[l]
    b = pre[n]-pre[l] - queries[i]*(n-l)
    arr.append(a+b)
print(arr)