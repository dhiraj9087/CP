import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=[]
    for _ in range(2):
        l=list(map(int,input().split()))
        a.append(l)
    best = [max(a[0][i],a[1][i]) for i in range(n)]
    full = [a[0][i]+a[1][i] for i in range(n)]
    add = sum(best)
    ans=float('-inf')
    for i in range(n):
        ans=max(ans,add+full[i]-best[i])
    print(ans)
for _ in range(int(input())):
   main()