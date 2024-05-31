import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans=0
    arr=[]
    mini=float('inf')
    ind=-1
    for i in range(n):
        ans += (abs(a[i]-b[i]))
        arr.append(abs(a[i]-b[i]))
        if abs(arr[i]-b[-1])<=mini:
            mini=abs(arr[i]-b[-1])
            ind=arr[i]
    
    # for i in range(n):
    #     if abs(arr[i]-b[-1])
for _ in range(int(input())):
   main()