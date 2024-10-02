from math import gcd,lcm
import sys
input=sys.stdin.readline
from functools import reduce


def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    same = all(i==k for i in a)
    if same:
        print(0)
        return
    
    start,end=-1,n
    for i in range(n):
        if a[i]!=k:
            if start == -1:
                start=i
            end=i
    if start==end:
        print(1)
        return
    xor = True
    divk = True
    s = a[start]^k
    for i in range(start,end+1):
        if a[i]%k!=0:
            divk = False
        if (a[i]^k )!= s:
            xor = False
    if xor or divk:
        print(1)
        return
    print(2)
    # print(6^2,6^4)
    # print(4^2,4^6)
    # print(1^2,1^3)
for _ in range(int(input())):
   main()