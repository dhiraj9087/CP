import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    bs,be=map(int,input().split())
    ans=bs
    for i in range(n-1):
        s,e=map(int,input().split())
        if s>=bs and e>=be:
            ans=-1
    print(ans)

for _ in range(int(input())):
   main()