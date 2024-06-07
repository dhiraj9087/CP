import math
import sys
input=sys.stdin.readline
def main():
    x,y=map(int,input().split())
    for i in range(30):
        if (x & (1 << i)) != (y & (1 << i)):
            print(1 << i)
            break
for _ in range(int(input())):
   main()