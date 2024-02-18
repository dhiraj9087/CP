import math
import sys
input=sys.stdin.readline
def main():
    nums = [3,2,1,2,3,4]
    # nums = [3,2,6,1,4]
    # nums=[1,9,7,3,2,7,4,12,2,6]
    n = len(nums)
    ans = 1
    a=nums.copy()
    b=nums.copy()
    print(a,b)
    s12,s1n,snn=nums[0]+nums[1],a[0]+a[n-1],b[n-1]+b[n-2]
    del nums[0]
    del nums[0]
    print(nums)
    while len(nums)>0:
        if len(nums)>=2 and nums[0]+nums[1]==s12:
            ans+=1
            del nums[0]
            del nums[0]
        elif len(nums)>=2 and nums[-1]+nums[-2]==s12:
            ans+=1
            del nums[-1]
            del nums[-1]
        elif len(nums)>=2 and nums[0]+nums[-1]==s12:
            ans+=1
            del nums[0]
            del nums[-1]
        else:
            break
    # print(ans)
    ans2=1
    del a[0]
    del a[-1]
    # # print(nums)
    while len(a)>0:
        if len(a)>=2 and a[0]+a[1]==s1n:
            ans2+=1
            del a[0]
            del a[0]
        elif len(a)>=2 and a[-1]+a[-2]==s1n:
            ans2+=1
            del a[-1]
            del a[-1]
        elif len(a)>=2 and a[0]+a[-1]==s1n:
            ans2+=1
            del a[0]
            del a[-1]
        else:
            break
    # print(ans2)
    ans3=1
    del b[0]
    del b[-1]
    # print(nums)
    while len(b)>0:
        if len(b)>=2 and b[0]+b[1]==snn:
            ans3+=1
            del b[0]
            del b[0]
        elif len(b)>=2 and b[-1]+b[-2]==snn:
            ans3+=1
            del b[-1]
            del b[-1]
        elif len(b)>=2 and b[0]+b[-1]==snn:
            ans3+=1
            del b[0]
            del b[-1]
        else:
            break
    print(ans,ans2,ans3)
# for _ in range(int(input())):
main()