import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=[i for i in range(1,n+1)]
    # print(a)
    for i in range(2,n):
        if a[i]==a[i-1]|a[i-2]:
            a[i],a[i-1]=a[i-1],a[i]
    print(*a)
for _ in range(int(input())):
   main()