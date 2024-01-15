def main():
    nums=[8,6,3,13,2,12,19,5,19,6,10,11,9]
    n=len(nums)
    maxi=float('-inf')
    a1=[0]*n
    a1[0]=nums[0]
    for i in range(1,n):
        a1[i] = max(nums[i],a1[i-1])
    a2=[0]*n
    a2[-1]=nums[-1]
    for i in range(n-2,-1,-1):
        a2[i]=max(a2[i-1],nums[i])

    for i in range(1,n-1):
        maxi=max(maxi,(a1[i-1]-nums[i])*a2[i+1])
    return maxi
    # a1,a2=[],[]
    # ans=float('-inf')
    # for i in nums:
    #     ans=max(ans,i)
    #     a1.append(max(ans-i,0))
    # print(a1)
    # n=len(nums)
    # maxi=nums[0]
    # ind=0
    # # if n<=3:
    # #     return 0
    # for i in range(1,n):
    #     if nums[i]>maxi:
    #         maxi=nums[i]
    #         ind=i
    #         break
    # if maxi==0:
    #     return 0
    # if n-ind<3:
    #     return 0
    # mini=float('inf')
    # ind2=0
    # for i in range(ind,n):
    #     if nums[i]<mini:
    #         mini=nums[i]
    #         ind2=i
    # maxi2=float('-inf')
    # for i in range(ind2,n):
    #     if nums[i]>maxi2:
    #         maxi2=nums[i]
    # print(maxi,mini,maxi2)
    # return (maxi-mini)*maxi2
print(main())