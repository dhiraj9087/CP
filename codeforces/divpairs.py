import math
import sys
input=sys.stdin.readline
from collections import defaultdict
def main():
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    d = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        d[a[i] % x][a[i] % y] += 1
    ans = 0
    for i in a:
        if (x - (i % x)) % x == (i%x):
            ans += d[(x - (i % x)) % x][i % y] - 1
        else:
            ans += d[(x - (i % x)) % x][i % y]
    print(ans // 2)
for _ in range(int(input())):
   main()