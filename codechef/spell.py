import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    for i in range(n-1):
        if s[i]>s[i+1]:
            print(s[:i]+s[i+1:])
            return
    print(s[:n-1])
for _ in range(int(input())):
   main()