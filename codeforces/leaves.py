import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    ans=0
    start = max(1,n-k+1)
    m = min(n,k)
    if start%2==1:
        odd = (m+1)//2
    else:
        odd = m//2
    print("YES" if odd%2==0 else "NO")
for _ in range(int(input())):
   main()