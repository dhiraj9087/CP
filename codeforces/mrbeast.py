import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print((a[n-1]-a[0]))
for _ in range(int(input())):
   main()