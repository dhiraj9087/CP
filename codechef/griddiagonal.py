import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    dig=4*n-2
    one=dig//2
    if k==dig:
        print(k//2 + 1)
        return
    if k%2==0:
        print(k//2)
        return
    print(k//2 + 1)
    
for _ in range(int(input())):
   main()