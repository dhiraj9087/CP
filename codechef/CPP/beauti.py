from collections import Counter
import math
import sys
input=sys.stdin.readline
mod=10**9 + 7
def main():
    n=int(input())
    s=input().strip()
    d=Counter(s)
    ans=1
    for i,j in d.items():
        ans = (ans*(j+1))%mod
    print(ans-1)


for _ in range(int(input())):
   main()