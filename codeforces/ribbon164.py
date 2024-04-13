import math
import sys
input=sys.stdin.readline
def main():
    n,m,k=map(int,input().split())
    # if 
    diff = n-math.ceil(n/m)
    if diff<=k:
        print("NO")
        return
    print("YES")
for _ in range(int(input())):
   main()