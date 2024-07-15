def onetimetwice():
    nums = [4,1,2,1,2]
    x=0
    for i in nums:
        x=x^i
    print(x)

def onetimethrice():
    nums = [5,5,5,6,6,6,4]
    ans=0
    # for i in range(32):
    #     c=0
    #     for j in range(len(nums)):
    #         if nums[j]&(1<<i):
    #             c+=1
    #     if c%3==1:
    #         ans = ans|(1<<i)
    # print(ans)
    nums.sort()
    for i in range(1,len(nums),3):
        if nums[i]!=nums[i-1]:
            print(nums[i-1])
            break
    

def twotimestwice():
    nums=[2,2,3,3,4,7,7,14]
    
    x=0
    for i in nums:
        x=x^i
    rightmost = (x&(x-1))^x
    l1,l2=0,0
    for i in range(len(nums)):
        if nums[i] & rightmost != 0:
            l1^=nums[i]
        else:
            l2^=nums[i]
    print(l1,l2)
twotimestwice()