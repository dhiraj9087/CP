import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ind=max(b)
    ans=a[:n-ind]+sorted(a[n-ind:])
    print(*ans)
for _ in range(int(input())):
   main()