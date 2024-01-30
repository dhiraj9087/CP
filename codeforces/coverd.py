import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    ans=""
    for i in range(n):
        for j in range(k):
            ans+=chr(ord('a')+j)
    print(ans)
for _ in range(int(input())):
   main()