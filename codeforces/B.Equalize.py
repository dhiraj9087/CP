import math
import sys
input=sys.stdin.readline
from bisect import bisect_right

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a=set(a)
    a=list(a)
    a=sorted(a)
    ans=0
    for i in range(len(a)):
        q=a[i]+n-1
        ind = bisect_right(a, q, lo=i) - i
        print(ind)
        ans=max(ans,ind)
    # print(ans)
for _ in range(int(input())):
   main()