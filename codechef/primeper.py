import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    if n < 4:
        print(-1)
        return
    start = 1
    rem = n % 4
    if rem == 1:
        print("4 5 1 2 3 ", end="")
        start = 6
    elif rem == 2:
        print("4 5 6 1 2 3 ", end="")
        start = 7
    elif rem == 3:
        print("6 7 1 2 3 4 5 ", end="")
        start = 8
    while start <= n:
        print(start + 2, start + 3, start, start + 1, end=" ")
        start += 4
    print()
for _ in range(int(input())):
   main()
