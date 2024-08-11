import math
import sys
input=sys.stdin.readline
def main():
    n,s,m=map(int,input().split())
    arr=[]
    for i in range(n):
        a,b=map(int,input().split())
        arr.append([a,b])
    if arr[0][0]>=s:
        print("YES")
        return
    if (m-arr[-1][1])>=s:
        print("YES")
        return
    for i in range(len(arr)-1):
        if (arr[i+1][0]-arr[i][1]) >= s:
            print("YES")
            return
    print("NO")
for _ in range(int(input())):
   main()