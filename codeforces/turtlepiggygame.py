import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    if n%2==1:
        print(a[n//2])
        return
    print(max(a[n//2-1],a[n//2]))
    
for _ in range(int(input())):
   main()