import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(0,n,2):
        ans=max(ans,a[i])
    print(ans)
for _ in range(int(input())):
   main()