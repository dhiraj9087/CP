import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans = f(a)
    print(ans)
for _ in range(int(input())):
   main()