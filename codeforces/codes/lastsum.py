import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    arr = a[:n]
    end = a[-1]
    arr.sort()
    add = sum(arr)
    # print(arr,add)
    for i in range(n):
        if arr[i]<=(2*end):
            if arr[i]>end:
                arr[i],end = end,arr[i]
    print(sum(arr))

for _ in range(int(input())):
   main()