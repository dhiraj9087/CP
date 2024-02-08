import math
import sys
input=sys.stdin.readline
mod=998244353
def main():
    n,k=map(int,input().split())
    print((2**k*(n-1))%mod)
for _ in range(int(input())):
   main()