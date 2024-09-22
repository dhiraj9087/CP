import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if n<=2:
        print(-1)
        return
    a.sort()
    mid = a[n//2]
    avg = sum(a)/(n*2)
    if avg>mid:
        print(0)
        return
    x = mid *n*2 - sum(a) + 1
    # print(x)
    largest = x
    avg2 = (sum(a) + largest) / (n*2)
    if avg2>mid:
        print(largest)
        return
    print(-1)
for _ in range(int(input())):
   main()