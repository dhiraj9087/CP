import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    if b%a==0:
        print(b*b//a)
        return
    print(math.lcm(a,b))

for _ in range(int(input())):
   main()