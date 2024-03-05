import math
import sys
input=sys.stdin.readline
def main():
    n,l=map(int,input().split())
    arr=[]
    for i in range(n):
        a,b=map(int,input().split())
        arr.append([a,b])
    arr.sort(key=lambda x: x[1])
    dp = [0]*(l+1)
    for i in range(1,n):
        for j in range(l,-1,-1):
            time=arr[i][0]+abs(arr[i][1]-arr[i-1][1])
            if j-time>=0:
                dp[j]=max(dp[j],dp[j-time]+1)

    print(dp[l])
for _ in range(int(input())):
   main()