import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    p=list(map(int,input().split()))
    # nums=[0]*n
    # for i in range(n):
    #     nums[i]=p[n-i-1]
    # # print(nums)
    # ans=0
    # for i in range(1,n):
    #     if p[i]<p[i-1]:
    #         ans+=1
    # print(ans)
    d={}
    for i in range(n):
        d[p[i]]=i
    # print(d)
    ans=0
    for i in p:
        if i!=1 and d[i]<d[i-1]:
            ans+=1
    print(ans)
   


for _ in range(int(input())):
   main()