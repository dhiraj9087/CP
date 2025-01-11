import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n<=3:
        print(1)
        return
    ans=1
    while n>3:
        n//=4
        ans*=2
    print(ans)
for _ in range(int(input())):
   main()