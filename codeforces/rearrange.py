import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    for i in a:
        s+=(abs(i))
    print(s)
for _ in range(int(input())):
   main()