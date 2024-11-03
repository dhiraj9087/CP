import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    one = s.count('1')
    zero = s.count('0')
    if zero==0:
        print(0 if one%2==0 else 1)
        return
    if one==0:
        print(n)
        return
    print(0 if one%2==0 else 1)
for _ in range(int(input())):
   main()