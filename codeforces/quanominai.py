import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1):
        if abs(a[i]-a[i+1]) != 5:
            if  abs(a[i]-a[i+1])!=7:
                print("NO")
                return
    print("YES")
for _ in range(int(input())):
   main()