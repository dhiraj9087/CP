import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    n=int(input())
    a=list(map(int,input().split()))
    # d=Counter(a)
    # s=list(set(a))
    # s.sort()
    # # print(s,s[-1]//2)
    # ind = s[-1]//2
    # ans=0
    # for i,j in d.items():
    #     if i<=ind:
    #         ans+=j
    # print(ans)
    a.sort()
    ans = n
    for i in range(n-1):
        left = i
        right = n-1
        ind = i+1
        while left<=right:
            mid = (left + right)//2
            if a[i] + a[i+1] > a[mid]:
                ind = mid
                left = mid+1
            else:
                right = mid-1
        ans = min(ans,n-(ind-i+1))
    print(ans)
for _ in range(int(input())):
   main()