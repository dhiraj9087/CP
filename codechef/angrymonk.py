import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    ans=0
    for i in range(k-1):
        if a[i]>1:
            ans+=(a[i]-1)
    l=ans
    ans += (k+l-1)
    print(ans)
for _ in range(int(input())):
   main()