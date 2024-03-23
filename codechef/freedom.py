import math
import sys
input=sys.stdin.readline
from collections import *
def main():
    n=int(input())
    a=list(map(int,input().split()))
    # l,r=0,1
    ans=0
    d=Counter()
    for i in range(n):
        ele=a[i]
        r = ele * 3
        ele2 = ele - 1
        if ele2 and r%ele2==0:
            ans += d[r//ele2]
        d[a[i]] += 1
    print(ans)
for _ in range(int(input())):
   main()

# 2*(a[i]) +  2*(a[j])==(a[i]-a[j]) + (a[i]*a[j])
# a[i] + 3*a[j] = a[i] * a[j]

# 1//a[j] + 2*a[j]//a[i] == 1