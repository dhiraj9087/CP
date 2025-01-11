import math
import sys
input=sys.stdin.readline
from collections import *
def main():
    n=int(input())
    s=input().strip()
    d=Counter(s)
    key=0
    maxi=-1
    mini=10000000000
    key2=0
    for i,j in d.items():
        if j>=maxi:
            maxi=j
            key=i
        if j<=mini:
            mini=j
            key2=i
    
    l=list(s)
    for i in range(n):
        if l[i]==key2:
            l[i]=key
            break
    print(''.join(l))
for _ in range(int(input())):
   main()