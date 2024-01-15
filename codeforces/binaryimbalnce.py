import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    arr=[]
    for i in range(n-1):
        arr.append(a[i]-a[i+1])
    # print(math.gcd(*arr))
    print(bin(205))
for _ in range(int(input())):
   main()