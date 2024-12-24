import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=a[n-1]
    for i in range(n-1):
        ans+=max(0,a[i]-b[i+1])
    print(ans)

for _ in range(int(input())):
   main()