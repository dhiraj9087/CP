import math
import sys
input=sys.stdin.readline
def main():
    n,k,x=map(int,input().split())
    k-=1
    if k>30:
        print("No")
        return
    if x >= (2**k):
        print("Yes")
        return
    print("No")
for _ in range(int(input())):
   main()