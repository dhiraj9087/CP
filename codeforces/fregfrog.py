import math
import sys
input=sys.stdin.readline
def main():
    x,y,k=map(int,input().split())
    ans=0
    mini = 2*((x+k-1)//k)-1
    maxi = 2*((y+k-1)//k)
    print(max(mini,maxi))
for _ in range(int(input())):
   main()