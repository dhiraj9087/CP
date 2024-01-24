import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    ans,add=0,0
    for i in range(n):
        add+=a[i]
        if add>=m:
            ans+=1
            add=0
    print(ans)
for _ in range(int(input())):
   main()