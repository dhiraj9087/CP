import math
import sys
input=sys.stdin.readline
def primediv():
    arr = [0] * 10000007
    arr[1] = 1
    for i in range(2, 10000007, 2):
        if arr[i] == 0:
            arr[i] += 1
            for j in range(2, 10000007 // i):
                arr[i * j] += 1
        if i == 2:
            i -= 1
    
def main():
    a=primediv()
    n=int(input())
    arr=list(map(int,input().split()))
    print(a)
    # s=set(a)

    # for i in range(1,10000007):
    #     if i not in arr and a[i]==1:
    #         print(i)
    #         return

for _ in range(int(input())):
   main()