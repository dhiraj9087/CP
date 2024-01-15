import math
import sys
input=sys.stdin.readline
def main():
    n,x,y,z=map(int,input().split())
    arr=[0]*(n+1)
    for i in range(1,n+1):
        if i >= x:
                arr[i] = max(arr[i], arr[i - x] + 1)
        if i >= y:
                arr[i] = max(arr[i], arr[i - y] + 1)
        if i >= z:
                arr[i] = max(arr[i], arr[i - z] + 1)





    
# for _ in range(int(input())):
main()