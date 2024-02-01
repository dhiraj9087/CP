import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    ans=k
    flag=False
    mini=float('inf')
    for i in range(n):
        if a[i]>=k:
            flag=True
            ans=min(ans,a[i]%k)
    if flag:
        print(ans)
        return
    print(-1)
for _ in range(int(input())):
   main()