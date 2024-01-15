import math
import sys
input=sys.stdin.readline
def main():
    a,b,c=map(int,input().split())
    d=(a+b)/2
    print(math.ceil(abs((d-a))/c))

for _ in range(int(input())):
   main()