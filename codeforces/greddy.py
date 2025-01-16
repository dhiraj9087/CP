# import math
# import sys
# input=sys.stdin.readline
# from collections import *
# def main():
#     n,k=map(int,input().split())
#     s=input().strip()
#     l=[]
#     add=0
#     for i in range(n-1,0,-1):
#         if s[i]=='1':
#             add+=1
#         else:add-=1
#         if add>0:
#             l.append(add)
#     # print(l)
#     l.sort()
#     ans=1
#     while k>0 and l:
#         k-=l.pop()
#         ans+=1
#     print(-1 if k>0 else ans)
# for _ in range(int(input())):
#    main()
def main():
    nums = [48,99,37,4,-31]
    k=140
    if k in nums:
        return 1
    if sum(nums)==k:
        return len(nums)
    pos=0
    for i in nums:
        if i>0:
            pos+=1
    print(pos)
    if pos<k:
        return -1
    print(pos)
    add=0
    n=len(nums)
    i=0
    ans=float('inf')
    for j in range(n):
        add+=nums[j]
        while add>=k:
            ans=min(ans,j-i+1)
            add-=nums[i]
            i+=1
            
    return ans,pos
print(main())