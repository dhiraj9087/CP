import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    # print(a)
    s=0
    l=n//2 if n%2==0 else n//2 + 1
    for i in range(l):
        s+=a[i]

    for i in range(l,n):
        s-=a[i]
    print(s)
for _ in range(int(input())):
   main()