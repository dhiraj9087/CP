import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n == 3:
        print("1 2 3")
    elif n % 2 == 0:
        for i in range(1, n // 2 + 1):
            print(i,n+1-i,end= ' ')
    else:
        for i in range(1, n // 2 + 1):
            print(i,n-i,end=' ')
        print(n)
for _ in range(int(input())):
   main()