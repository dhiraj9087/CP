import math
import sys
input=sys.stdin.readline
def main():
    n,h=map(int,input().split())
    a=list(map(int,(input().split())))
    if sum(a)<h:
        print(0)
        return
    a.sort()
    ans=0
    for i in range(n-1,-1,-1):
        ans+=a[i]
        if ans>=h:
            print(a[i])
            return
for _ in range(int(input())):
   main()