import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    d=Counter(a)
    freq=d[k]
    if freq>=(n//2):
        print(0)
        return
    if a[0]==k or a[-1]==k:
        print(1)
        return
    d2=Counter(a)
    ans=False
    for i in range(n-1):
        ele = a[i]
        d2[ele]-=1
        maxi=max(d2.values())
        if maxi==d2[k]:
            ans=True
            break
    d3=Counter(a)
    for i in range(n-1,0,-1):
        ele = a[i]
        d3[ele]-=1
        maxi=max(d3.values())
        if maxi==d3[k]:
            ans=True
            break
    if ans==True:
        print(1)
        return
    print(2)
    # left,right=-1,-1
    # for i in range(n):
    #     if a[i]==k:
    #         left=i
    #         break
    # for i in range(n-1,-1,-1):
    #     if a[i]==k:
    #         right=i
    #         break
    # if left==right:
    #     if left<2 or right>n-3:
    #         print(1)
    #         return
    #     print(2)
    #     return
    # if a[0:left+1].count(3) >= (len(a[0:left+1])/2):
    #     print(1)
    #     return
    # if a[left:].count(3) >= (len(a[left:])/2):
    #     print(1)
    #     return
    # if a[0:right+1].count(3)>=(len(a[0:right+1])/2):
    #     print(1)
    #     return
    # if a[right:].count(3) >= len(a[right:])/2:
    #     print(1)
    #     return
    # print(2)
    # left_rem,right_rem = n-left,n-(n-right)+1
    # # print(left,left_rem,right,right_rem)
    # if freq>=(left_rem/2):
    #     print(1)
    #     return
    # if freq>=(right_rem/2):
    #     print(1)
    #     return
    # arr = a[left:right+1]
    # if freq>=(len(arr)/2):
    #     print(2)
    #     return
    # print(3)
    # print(arr,left_rem,right_rem)
for _ in range(int(input())):
   main()