import math
import sys
from collections import *
input=sys.stdin.readline

def main():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    maxi=2*sum(a)
    add=sum(a)
    d=Counter(a)
    for _ in range(x):
        q=int(input())
        s1,s2=-1,-1
        for i in range(n):
            rem=maxi-q-a[i]
            if rem==a[i]:
                if d[a[i]]>1:
                    s1,s2=rem,rem
                    break
            else:
                if d[rem]:
                    s1=rem
                    s2=a[i]
                    break
        if s1==-1 and s2==-1:
            print(-1)
        else:
            flag1,flag2=True,True
            print(s1,end=" ")
            for i in range(n):
                if a[i]==s1 and flag1==True:
                    flag1=False
                elif a[i]==s2 and flag2==True:
                    flag2=False
                else:
                    print(a[i],end=" ")
            print(s2)

for _ in range(int(input())):
   main()