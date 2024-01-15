import math
import sys
input=sys.stdin.readline
def main():
    n = int(input())
    ans=[2]
    for i in range(1, n):
        ans.append(ans[i-1]+3)
    print(*ans)
for _ in range(int(input())):
   main()