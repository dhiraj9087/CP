import math
import sys
input=sys.stdin.readline
mod=10**9 + 7
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    ans=a[0]
    for i in range(1,n):
        if  (a[i] == 1) or (a[i] == 0 ) or (ans <= 1 and a[i] > 1):
                ans = (ans + a[i]) % mod
        else:
            ans = (ans * a[i]) % mod
    print(ans%mod)
for _ in range(int(input())):
   main()