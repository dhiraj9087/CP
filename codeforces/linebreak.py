import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    ans=0
    a=0
    for _ in range(n):
        s=input().strip()
        a+=len(s)
        if a<=m:
            ans+=1
    print(ans)
for _ in range(int(input())):
   main()