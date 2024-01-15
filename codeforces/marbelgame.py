import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    arr = []
    for i in range(n):
        arr.append([a[i]+b[i],i])
    arr.sort(reverse=True)
    ans1,ans2 = 0,0
    for i in range(n):
        if i % 2 == 0:
            ans1 += (a[arr[i][1]] - 1)
        else:
            ans2 += (b[arr[i][1]] - 1)
    print(ans1-ans2)
for _ in range(int(input())):
   main()