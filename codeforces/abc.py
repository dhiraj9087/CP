import math
import sys
input=sys.stdin.readline
def main():
    a=int(input())
    if a==2:
        print(4,8)
        return
    print(a*2,a*a)
for _ in range(int(input())):
   main()