import math
import sys
input=sys.stdin.readline
from collections import *
def main(): 
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print(0)
        return
    d=Counter(a)
    maxi=max(d.values())
    ind=float('inf')
    for i,j in d.items():
        if j==maxi:
            if i<ind:
                ind=i
    # print(ind)
    ans=0
    s1,s2=0,0
    arr=[]
    flag=True
    l,r=0,0
    i=0
    while i < n:
        if a[i] == ind:
            i += 1
        else:
            L = i
            while i < n and a[i] != ind:
                i += 1
            R = i - 1
            ans += (R - L + 1) * ind
    num=0
    for i in range(n):
        if a[i]!=1:
            num+=1
    print(min(ans,num))
for _ in range(int(input())):
   main()