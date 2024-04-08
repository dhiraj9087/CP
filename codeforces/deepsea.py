import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    add=sum(a)
    if add<=k:
        print(n)
        return
    pref = 0
    pref_sum = 0
    while pref_sum <= k // 2 + k % 2:
        pref_sum += a[pref]
        pref += 1
    suf = -1
    suf_sum = 0
    while suf_sum <= k //2:
        suf_sum += a[suf]
        suf -= 1
    print(pref - 1 - suf - 2)
    
for _ in range(int(input())):
   main()