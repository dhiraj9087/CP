import math
import sys
input=sys.stdin.readline
def main():
    n,k,x=map(int,input().split())
    if n<k or x+1<k:
        print(-1)
        return
    ans=0
    for i in range(k):
        ans+=i
    if x==k:
        x-=1
    for i in range(n-k):
        ans+=x
    print(ans)
for _ in range(int(input())):
   main()