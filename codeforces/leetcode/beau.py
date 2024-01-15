def main():
    nums = [2,3,0,0,2]
    k = 4
    # nums = [0,1,3,3]
    # k = 5
    # nums = [1,1,2]
    # k = 1
    nums=[1,2,6,9]
    k=8
    # nums=[2,35,41,20]
    # k=4
    # nums=[10,2,0,2]
    # k=6
    # nums = [2, 1, 4, 2, 5, 3, 6]
    # k = 4
    # nums = [3, 2, 1, 4, 6, 2, 7, 5]
    # k = 5   
    nums=[43,31,14,4]
    k=73
    nums.append(k)
    n = len(nums)
    best = [0]
    for i in range(n):
        curr = max(0, k - nums[i])
        curr += min(best[-3:])
        best.append(curr)
    return best[-1]
    # n=len(nums)
    # ans=0
    # a=[]
    # if n<=3 and max(nums)>=k:
    #     print(0)
    #     return
    # if n<=3 and max(nums)<k:
    #     print(k-max(nums))
    #     return
    # if n==4:
    #     e=sorted(nums)
    #     z=sorted(nums,reverse=True)
    #     # print(e,z)
    #     if e==nums:
    #         if max(nums[0:3])>=k:
    #             print(0)
    #             return
    #         ans+= (k-max(nums[0:3]))
    #         print(ans)
    #         return
    #     if z==nums:
    #         if max(nums[1:4])>=k:
    #             print(0)
    #             return
    #         ans+= (k-max(nums[1:4]))
    #         print(ans)
    #         return
    #     if max(nums[0:3])>=k:
    #         if max(nums[1:4])>=k:
    #             print(0)
    #             return
    #         ans+= (k-max(nums[1:4]))
    #         print(ans)
    #         return
    #     ans+= (k-max(nums[0:3]))
    #     print(ans)
    #     return
    # if n==5 and nums[]
    # for i in range(0,n,3):
    #     a=nums[i:i+3]
    #     print(a)
    #     maxi=max(a)
    #     maxi_ind=a.index(maxi)
    #     if maxi<k:
    #         ans+=(k-maxi)
            
    # print(ans)
    # # if n<=3 and min(nums)>=k:
    # #     print(0)
    # #     return
    # # if n==4:
    # #     ans+= (k-max(nums))
    # #     print(ans)
    # #     return
    # # for i in range(0,n,3):
    # #     # print(nums[i:i+3])
    # #     maxi=max(nums[i:i+3])
    # #     mini=min(nums[i:i+3])
    # #     if mini>=k:
    # #         continue
    # #     else:
    # #         ans+= (k-maxi)
    # # print(ans)

main()