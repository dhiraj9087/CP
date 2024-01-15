

# def solve():
#     nums = [10,1,2,7,1,3]
#     p = 2
#     # nums = [4,2,1,2]
#     # p = 1
#     n=len(nums)
#     nums.sort()
#     print(nums)
#     maxi=float('-inf')
#     mini=float('-inf')
#     for i in range(1,n-1,2):
#         maxi=max(maxi,max(abs(nums[i]-nums[i-1]),abs(nums[i+1]-nums[i])))
#     print(maxi)
#     a=[]
#     c=0
#     # for i in range(0,n,2):
#     #     if abs(nums[i]-nums[i+1])<maxi and c<=p:
#     #         a.append(abs(nums[i]-nums[i+1]))
#     #         c+=1
    
#     # print(max(a))
        


# solve()
s=[0]+[*map(int,list(input()))]