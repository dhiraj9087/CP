import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    p=list(map(int,input().split()))
    a=[0]*n
    if n<=2:
        print(-1)
        return
    for i in range(n):
        if p[i]==1:
            a[i]=3
        elif p[i]==3:
            a[i]=1
        else:
            a[i]=p[i]
    print(*a)
for _ in range(int(input())):
   main()