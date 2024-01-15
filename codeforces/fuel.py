import math
import sys
input=sys.stdin.readline
def main():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    ans=a[0]
    for i in range(n-1):
        ans=max(ans,a[i+1]-a[i])
    ans=max(ans,2*abs(x-a[n-1]))
    print(ans)
for _ in range(int(input())):
   main()