import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    square_root = math.isqrt(sum(a))
    if square_root * square_root == sum(a):
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
   main()