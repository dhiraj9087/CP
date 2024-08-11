import math
import sys
input=sys.stdin.readline

def main():
    n=int(input())
    a=list(map(int,input().split()))
    arr=[0]*n
    for i in range(n):
        arr[i]=a[(i+1)%n]
    print(*arr)
for _ in range(int(input())):
   main()