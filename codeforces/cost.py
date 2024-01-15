import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    if k not in a:
        print("NO")
        return
    print("YES")
for _ in range(int(input())):
   main()