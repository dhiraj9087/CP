import math
import sys
input=sys.stdin.readline
from collections import *

def mode(s):
    d=Counter(s)
    maxi=max(d.values())
    c=0
    for i,j in d.items():
        if j==maxi:
            c+=1
    return c

def main():
    n=int(input())
    s=input().strip()
    # arr=[]
    ans=0
    ans+= n*(n+1)//2
    d={0:1}
    c1,c2=0,0
    for i in s:
        if i=='0':
            c1+=1
        else:
            c2+=1
        a=c1-c2
        if a in d:
            ans+=d[a]
            d[a]+=1
        else:
            d[a]=1
    print(ans)
for _ in range(int(input())):
   main()


