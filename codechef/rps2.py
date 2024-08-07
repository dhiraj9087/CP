import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    x=n//9
    rem=n%9
    print(x*45 + rem*(rem+1)//2)
for _ in range(int(input())):
   main()