import math
import sys
input=sys.stdin.readline
def main():
    x,y,k=map(int,input().split())
    if x>=y:
        print(x)
        return
    if x+k>=y:
        print(y)
        return
    print(2*(y-(x+k))+(x+k))
for _ in range(int(input())):
   main()