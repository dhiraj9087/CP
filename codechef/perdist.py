import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in range(n-1):
        if a[i]==i+1:
            a[i],a[i+1]=a[i+1],a[i]
            ans+=1
    if a[-1]==n:
        ans+=1
    print(ans)
for _ in range(int(input())):
   main()