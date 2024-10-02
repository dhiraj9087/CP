import math
import sys
input=sys.stdin.readline
def main():
    input1=3
    n=input1
    mod = 1e9+7
    arr=[0]*(n+1)
    arr[0]=1
    arr[1]=1
    for i in range(2,n+1):
        arr[i] = (arr[i-1] + 7*(arr[i-2]) + (i//4))%mod
    print(arr[n])
for _ in range(int(input())):
   main()