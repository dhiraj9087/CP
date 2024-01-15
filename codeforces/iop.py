from collections import Counter
import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=input().strip()
    d=Counter(a)
    maxi=max(d.values())
    print(max(n%2,2*maxi-n))
for _ in range(int(input())):
   main()