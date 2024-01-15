import math
import sys
input=sys.stdin.readline


def main():
    n=int(input())
    c=[]
    l=[]
    for i in range(n):
        m=int(input())
        a=list(map(int,input().split()))
        c.append(m)
        l.append(a)
    print(c,l)
    
for _ in range(int(input())):
    main()