import math
import sys
input=sys.stdin.readline
def main():
    n,a,b=map(int,input().split())
    ans=0
    if (2*a)>b:
        if n%2==0:
            ans+=(b*(n//2))
            print(ans)
            return
        if n%2==1:
            ans+=(b*(n//2))
            print(ans+a)
            return
    else:
        print(n*a)
        return
for _ in range(int(input())):
   main()