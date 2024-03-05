import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    if s<=s[::-1]:
        print(s)
        return
    print(s[::-1]+s)
for _ in range(int(input())):
   main()