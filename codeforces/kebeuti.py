import math
import sys
input=sys.stdin.readline
def add(a):
    s=0
    while a>0:
        d=a%10
        s+=d
        a//=10
    return s
def main():
    x,k=map(int,input().split())
    for i in range(x,10**9 + 10):
        if add(i)%k==0:
            print(i)
            return
for _ in range(int(input())):
   main()