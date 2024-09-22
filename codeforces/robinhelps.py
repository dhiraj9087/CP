import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    coin=0
    ans=0
    for i in range(n):
        if a[i]>=k:
            coin+=a[i]
        if a[i]==0 and coin>0:
            ans+=1
            coin-=1
    print(ans)
for _ in range(int(input())):
   main()