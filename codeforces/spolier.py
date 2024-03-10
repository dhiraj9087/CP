import math
import sys
input=sys.stdin.readline
def main():
    nums = [1,2,3,-1,2]
    k = 3
    # nums = [12,-2,-2,-2,-2]
    # k = 5
    # nums = [-1,-2,-3]
    # k = 1
    n=len(nums)
    neg=sum(1 for i in nums if i<0)
    print(neg)
    first=0
    ind=-1
    for i in range(n):
        if nums[i]>0:
            first+=nums[i]
        else:
            first*=(i)
            ind=i
            break
    sec=0
    ind2=-1
    for i in range(ind,n):
        if nums[i]<=0:
            sec+=nums[i]
        else:
            sec*=(i)
            ind2=i
            break
    print(first)


# for _ in range(int(input())):
main()