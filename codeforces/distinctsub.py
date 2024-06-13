import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    if n==k==1:
        print("YES")
        return
    zero=k*(k+1)//2
    zero += (k-1)
    print("YES" if n>=zero else "NO")
for _ in range(int(input())):
   main()   