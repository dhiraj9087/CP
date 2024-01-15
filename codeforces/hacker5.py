import math
import sys
input=sys.stdin.readline
def main():
    D,d,x,y=map(int,input().split())
    amt=0
    c =0
    for i in range(1,D+1):
        c = x + (math.ceil(i / d) - 1) * y
        amt += c
    print(amt)    
for _ in range(int(input())):
    main()
    