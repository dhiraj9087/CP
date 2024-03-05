import math
import sys
input=sys.stdin.readline
from collections import Counter
def fun(arr):
    i = 0
    while i in arr:
        i += 1
    return i
def main():
    n=int(input())
    a=list(map(int,input().split()))
    # if len(set(a))==1:
    #     print(n)
    #     for i in range(1,n+1):
    #         print(i,i)
    #     return
    # maxi,count=0,0
    # d=Counter(a)
    mex=fun(a)
    # if a[0]==a[-1]==0 or mex>max(a):
    #     print(-1)
    #     return
    # print(mex)
    l,r=0,0
    arr=[]
    arr=sorted(a)
    ans=mex
    s=set()
    for i in range(n):
        if a[i]<ans:
            s.add(a[i])
        if len(s)==ans:
            r=i+1
            break
    s2=set()
    flag=True
    for i in range(r,n):
        if a[i]<ans:
            s2.add(a[i])
        if len(s2)==ans:
            flag=False
            break
    if flag:
        print(-1)
        return
    print(2)
    print(1,r)
    print(r+1,n)

for _ in range(int(input())):
   main()