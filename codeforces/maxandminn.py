import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    ans=n*(n+1)//2
    ans+=(n-1)
    print(ans)
for _ in range(int(input())):
   main()