import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    t1,t2=float('inf'),float('inf')
    ans=0
    for i in range(n):
        if t1>t2:
            t1,t2=t2,t1
        if a[i] <= t1:
            t1 = a[i]
        elif a[i] <= t2:
            t2 = a[i]
        else:
            t1 = a[i]
            ans += 1
    print(ans)
for _ in range(int(input())):
   main()