import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    arr=[]
    for i in range(n):
        a=list(map(int,input().split()))
        arr.append(a)
    ans=arr
    if n==1 and m==1:
        print(-1)
        return
    for i in range(n-1):
        arr[i],arr[i+1] = arr[i+1],arr[i]
    for i in range(len(arr)):
        for j in range(len(arr[i])-1):
            arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end=" ")
        print()
    # print(arr)
for _ in range(int(input())):
   main()