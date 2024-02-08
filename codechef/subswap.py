import math
import sys
input=sys.stdin.readline
def main():
    x,y=map(int,input().split())
    print(math.gcd(x,y))
for _ in range(int(input())):
   main()