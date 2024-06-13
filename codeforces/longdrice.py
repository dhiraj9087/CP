import math
import sys
input=sys.stdin.readline
def main():
    x,y=map(int,input().split())
    ans=math.ceil(10 * (y - x) / (100 - y))
    print(ans)
for _ in range(int(input())):
   main()