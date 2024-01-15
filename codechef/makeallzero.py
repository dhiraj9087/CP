import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    arr=[a[0]]
    for i in range(1,n):
        if a[i]<=arr[-1]:
            arr.append(a[i])
    # print(arr)
    ans=n
    for i in range(len(arr)-1,-1,-1):
        ans=min(ans,n-len(arr)+i+arr[i])
    print(ans)
for _ in range(int(input())):
   main()