import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    print(max(a)-min(a))

for _ in range(int(input())):
   main()