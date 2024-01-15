def main():
    nums = [1,2,3]
    target = 5
    # nums = [1,1,1,2,3]
    # target = 4
    # nums = [2,4,6,8]
    # target = 3
    n=len(nums)
    add=sum(nums)
    if add==target:
        print(n)
        return
    if add>target:
        a=0
        for i in range(n):
            a+=nums[i]
            ind=0
            while a>target:
                a-=nums[ind]
                if a==target:
                    print(i+1)
                    return
                a+=nums[i]
        print(-1)
        return
    


main()