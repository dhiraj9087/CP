import math
import sys
input=sys.stdin.readline
from collections import Counter

def main():
    n=int(input())
    a=list(map(int,input().split()))
    if 1 not in a:
        print("NO")
        return
    a.sort()
    for i in range(n):
        num = i + 1
        if a[i] > num:
            print("NO")
            return
    print("YES")
    
for _ in range(int(input())):
   main()