import math
import sys
input=sys.stdin.readline

def isPowerofTwo(n):
    return n != 0 and (n & (n - 1)) == 0
def main():
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-1):
        if isPowerofTwo(i+1):
            continue
        if a[i]>a[i+1]:
            print("NO")
            return
    print("YES")
    
for _ in range(int(input())):
   main()