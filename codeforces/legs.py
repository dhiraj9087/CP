import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n%4==0:
        print(n//4)
        return
    if n<4:
        print(1)
        return
    print(math.ceil(n/4))
for _ in range(int(input())):
   main()