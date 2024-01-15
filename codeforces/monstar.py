import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    q=sum(a)
    a.sort(reverse=True)
    s=0
    ans,x=q,0
    for i in range(n):
        s+=a[i]
        q-=a[i]
        if s>q:
            x=s-q
            x=(x+1)//2
        res=q+x
        ans=min(ans,i+1+res)
        x=0
    print(ans)
for _ in range(int(input())):
   main()