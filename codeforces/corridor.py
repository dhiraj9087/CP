import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    ans=float('inf')
    for i in range(n):
        d,s=map(int,input().split())
        a=d+(s-1)//2
        ans=min(ans,a)
    print(ans)
for _ in range(int(input())):
   main()