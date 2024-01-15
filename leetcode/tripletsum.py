def main():
    # nums = [8,6,1,5,3]
    # nums = [5,4,8,7,10,2]
    # nums = [6,5,4,3,4,5]
    # nums=[1,3,1,2]
    nums=[1,2,3,5,4]
    n=len(nums)
    l,r=0,float('inf')
    ind=0
    a=sorted(nums)
    if nums==a or nums==a[::-1]:
        return -1
    for i in range(1,n):
        if nums[i]>nums[i-1]:
            ind=i
            l=nums[i-1]
            break
    ind2=0
    for i in range(n-1,ind,-1):
        if r>nums[i]:
            r=nums[i]
            ind2=i
        # r=min(r,nums[i])
            
    ans=float('inf')
    for i in range(ind,ind2+1):
        print(nums[i])
        if nums[i]>l and nums[i]>r:
            ans=min(ans,l+r+nums[i])
    print(l,r,ind,ind2,ans)
    # return ans if ans!=inf elsme -1
    

main()