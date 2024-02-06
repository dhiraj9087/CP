import math
import sys
input=sys.stdin.readline
from collections import Counter
lim=10**6
def main():
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    # a.sort()
    # b.sort()
    x,y,z=0,0,0
    a=set(a)
    b=set(b)
    arr=set()
    for i in a:
        if i<=k:
            x+=1
            arr.add(i)
    for i in b:
        if i<=k:
            y+=1
            arr.add(i)
    for i in arr:
        if i<=k:
            z+=1
    if z==k:
        if x>=k//2 and y>=k//2:
            print("YES")
            return
        print("NO")
        return
    
    print("NO")
for _ in range(int(input())):
   main()