import math
import sys
input=sys.stdin.readline
def main():
    l,r=map(int,input().split())
    print(((r + 1) // 2 - l // 2) // 2)

for _ in range(int(input())):
   main()