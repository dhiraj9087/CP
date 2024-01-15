import math
import sys
input=sys.stdin.readline
def main():
    n,x=map(int,input().split())
    if x==n-x+1:
        print(-1)
        return
    ans=[i for i in range(1,n+1)]
    if x==1:
        print(*ans)
        return
    if x==n:
        ans=sorted(ans,key=lambda x:x ,reverse=True)
        print(*ans)
        return
    a,b=ans.remove(x),ans.remove(n-x+1)
    ans=[x]+ans+[n-x+1]
    print(*ans)
for _ in range(int(input())):
   main()