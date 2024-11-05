import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    if n==1:
        print(1)
        print(1)
        return
    # if (n//2)+1 != k:
    #     print(-1)
    #     return
    if k==1 or k==n:
        print(-1)
        return
    if k%2==0:
        print(3)
        print(1,k,k+1)
        return
    print(5)
    print(1,2,k,k+1,k+2)
for _ in range(int(input())):
   main()