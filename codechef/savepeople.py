import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    ans=[(x-1)*m,(y-1)*n,(m-y)*n,(n-x)*m]
    print(max(ans))
for _ in range(int(input())):
   main()