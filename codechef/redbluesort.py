import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if a==sorted(a):
        print(n)
        return
    flag=False
    for i in range(n):
        if a[i]==i+1:
            flag=True
            break
    if flag:
        print(n-1)
        return
    print(n-2)
for _ in range(int(input())):
   main()