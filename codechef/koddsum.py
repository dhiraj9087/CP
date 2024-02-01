import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    ans=[]
    for i in range(1, k + 1):
        ans.append(i)
    for i in range(k + 2, n + 1, 2):
        ans.append(i)
    for i in range(k + 1, n + 1, 2):
        ans.append(i)
    print(*ans)
for _ in range(int(input())):
   main()