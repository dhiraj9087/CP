import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    for i in range(k):
        if a[i]==1:
            a[i]=6
        elif a[i]==2:
            a[i]=5
        elif a[i]==3:
            a[i]=4
    print(sum(a))
for _ in range(int(input())):
   main()