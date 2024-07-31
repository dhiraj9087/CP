import math
import sys
input=sys.stdin.readline
# from functools import reduce

def main():
    n=int(input())
    a=list(map(int,input().split()))
    maxi=max(a)
    for i in range(n):
        if a[i]!=maxi and a[i]!=0:
            print("NO")
            return
    print("YES")
for _ in range(int(input())):
   main()