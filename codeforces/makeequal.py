import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    n=int(input())
    a=list(map(int,input().split()))
    d=Counter(a)
    x,y = 0,0
    for i in range(n - 1, -1, -1):
        if a[i] == a[n - 1]:
            y += 1
        else:
            break
    for i in range(n):
        if a[i] == a[0]:
            x += 1
        else:
            break
    if x == n:
        print(0)
        return
    if a[0] == a[n - 1]:
        print(n - x - y)
        return
    print(n - max(x, y))

for _ in range(int(input())):
   main()