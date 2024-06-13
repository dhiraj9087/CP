import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    ans=[]
    for i in range(n-1):
        ans.append(n)
    ans.append(1)
    print(*ans)
for _ in range(int(input())):
   main()