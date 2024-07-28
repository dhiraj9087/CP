import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    ans=0
    a, b = n, n - 1
    ans = 0
    while k > 0:
        k -= a
        ans += 1
        a, b = b, (b if a != b else b - 1)
    print(ans)
 
for _ in range(int(input())):
   main()