import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    add=0
    d=set()
    for i in range(n):
        add+=a[i]
        d.add(a[i])
        if add%2==0:
            req=add//2
            if req in d:
                ans+=1
    print(ans)
for _ in range(int(input())):
   main()