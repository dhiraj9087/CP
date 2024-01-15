import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=input()
    b=input()
    # N,M=map(int,input().split())
    # S=input()
    # K=input()
    # N = len(S)
    # M = len(K)
    ans = float('inf')

    for i in range(n - m + 1):
        s = 0
        for j in range(m):
            diff = abs(int(a[i + j]) - int(b[j]))
            s += min(diff, 10 - diff) 
        ans= min(ans, s)
    print(ans)
for _ in range(int(input())):
   main()


