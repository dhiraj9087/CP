import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    ans=0
    while n:
        if n & 1:
            ans+=1
        n >>= 1
    print(ans)
# for _ in range(int(input())):
main()