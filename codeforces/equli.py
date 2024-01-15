from collections import Counter
import math
import sys
input=sys.stdin.readline
def main():
    nums = [1,2,3,4,5]
    nums = [10,12,13,14,15]
    # nums = [22,33,22,33,22]
    n=len(nums)
    d=Counter(nums)
    maxi=max(d.values())
    ele=0
    for i ,j in d.items():
        if j==maxi:
            ele=i
    if len(set(nums))!=n:
        ans=0
        for i in range(n):
            if nums[i]!=ele:
                ans+=(abs(nums[i]-ele))
        return ans
    

# for _ in range(int(input())):
print(main())