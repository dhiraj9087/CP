import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    l,r=0,0
    ele=0
    for i in range(n):
        ele+=a[i]
        if ele>=m:
            l+=1
            ele=0
    print(l)
for _ in range(int(input())):
   main()