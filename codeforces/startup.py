import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    arr=[0]*k
    for i in range(k):
        b,c=map(int,input().split())
        arr[b-1] += c
    arr.sort(reverse=True)
    ans=0
    for i in range(min(n,k)):
        ans+=arr[i]
    print(ans)
for _ in range(int(input())):
   main()