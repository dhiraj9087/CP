import math
import sys
input=sys.stdin.readline
def main():
    n,f,a,b=map(int,input().split())
    s=[0]+list(map(int,input().split()))
    ans=f
    for i in range(n):
        val=min((s[i+1]-s[i])*a,b)
        ans-=val
    print("NO" if ans<=0 else "YES")
for _ in range(int(input())):
   main()