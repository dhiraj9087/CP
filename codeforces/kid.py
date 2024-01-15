import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if 0 in a:
        print(0)
        return
    mini=float('inf')
    for i in a:
        if abs(i)<mini:
            mini=abs(i)
    print(mini)


# for _ in range(int(input())):
main()