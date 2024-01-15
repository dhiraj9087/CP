import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=[n]
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=n*3 + 1
        a.append(n)
    print(*a)
# for _ in range(int(input())):
main()