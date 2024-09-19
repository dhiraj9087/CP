import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    print("NO" if s[0]==s[-1] else "YES")
for _ in range(int(input())):
   main()