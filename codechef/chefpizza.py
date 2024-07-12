import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    ab = 1
    while ab <= n:
        ab <<= 1
    if ab == n:
        print(0)
        return
    ab >>= 1
    difference = n - ab
    result = difference * 2
    print(result)
for _ in range(int(input())):
   main()