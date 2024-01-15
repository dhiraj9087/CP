import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for i in range(n):
        x^=a[i]
    ans = x
    for i in range(n):
        t= x ^ a[i]
        ans = min(ans, t)

    print(ans)
for _ in range(int(input())):
   main()