import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    maxi = 0
    ans = 2
    for x in range(2, n + 1):
        k = n // x
        curr = x * (k * (k + 1) // 2)
        
        if curr > maxi:
            maxi = curr
            ans = x
    print(ans)
        
for _ in range(int(input())):
   main()