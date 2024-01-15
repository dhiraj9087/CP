import math
import sys
input=sys.stdin.readline
def main():
    n,x,y=map(int,input().split())
    a=[0]*n
    for i in range(n):
        if i%x==0:
            a[i]=n-i
    print(a)
for _ in range(int(input())):
   main()