import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=a[0]
    for i in range(1,n):
        ans*=a[i]
    print((ans+(n-1))*2022)
for _ in range(int(input())):
   main()

   