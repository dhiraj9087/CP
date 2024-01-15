import math
import sys
input=sys.stdin.readline
def main():
    n,x,k=map(int,input().split())
    b,g=x,n-x
    remb,reg=b%k,g%k
    print(abs(remb-reg))
for _ in range(int(input())):
   main()