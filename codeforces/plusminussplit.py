import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    print(abs(s.count('+')-s.count('-')))
for _ in range(int(input())):
   main()