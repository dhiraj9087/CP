import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    ans = (n + k - 1) // k
    k *= ans
    print((k + n - 1) // n)


for _ in range(int(input())):
   main()