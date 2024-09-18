import math
import sys
input=sys.stdin.readline
def main():
    l,r = map(int,input().split())
    i=1
    while l + (i * (i-1)) // 2 <= r:
        i += 1
    print(i-1)
for _ in range(int(input())):
   main()