import math
import sys
input=sys.stdin.readline

    

def main():
    x,y,k=map(int,input().split())
    z = k // 2
    for i in range(z):
        print(x - i - 1, y)
        print(x + i + 1, y)
    if k % 2 == 1:
        print(x, y)
for _ in range(int(input())):
   main()
