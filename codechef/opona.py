import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(1,n-2):
        arr=a
        arr[i-1]=(a[i-1]+a[i]+a[i+1])
        arr[i]=(-a[i+1])
        arr[i+1]=(-a[i])
        arr[i+2]=(a[i+2]+a[i+1]+a[i])
        if arr==b:
            print("YES")
            return
    print("NO")
for _ in range(int(input())):
   main()