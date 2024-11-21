import math
import sys
input=sys.stdin.readline
def main():
    x,y,k=map(int,input().split())
    m = min(x,y)
    print(0,0,m,m)
    print(0,m,m,0)
     
for _ in range(int(input())):
   main()