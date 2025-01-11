import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in range(n):
        if a[i] in d:
            d[a[i]]=i+1
        else:
            d[a[i]]=i+1
    ans=0
    for i,j in d.items():
        ans+=j
    print(ans)
for _ in range(int(input())):
   main()