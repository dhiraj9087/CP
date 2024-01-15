import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a[0]=a[0]+1
    ad=1
    for i in a:
        ad = ad*i
    print(ad)
for _ in range(int(input())):
   main()