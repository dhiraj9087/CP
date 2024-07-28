import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    arr=[]
    for _ in range(n):
        s=input().strip()
        arr.append(s)
    # print(arr)
    for i in range(0,n,k):
        for j in range(0,n,k):
            print(arr[i][j],end='')
        print()
for _ in range(int(input())):
   main()