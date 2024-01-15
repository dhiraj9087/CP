import math
import sys
input=sys.stdin.readline
def main(s):
    n=int(input())
    a=list(map(int,input().split()))
    if s==0:
        a1=sorted(a)
        ans=0
        if n%2==1:
            for i in range(n//2+1):
                ans+=a1[i]
            print(ans)
            return
        for i in range(1,n//2+1):
            ans+=a1[i]
        print(ans)
        return
    if s==1:
        a1=sorted(a,key=lambda x:x,reverse=True)
        arr=[0]*(n+1)
        for i in range(n):
            arr[i+1]=arr[i]+a1[i]
        ans=0
        for i in range(n):
            if i+i+1>n:
                break
            ans=max(ans,arr[i+i+1]-arr[i])
        print(ans)
        return
# for _ in range(int(input())):
t,s=map(int,input().split())
for _ in range(t):
   main(s)