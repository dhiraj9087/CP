import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=str(n)
    ans=0
    for i in s:
        ans+=int(i)
    print(ans)
for _ in range(int(input())):
   main()