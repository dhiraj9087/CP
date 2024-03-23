import math
import sys
input=sys.stdin.readline

def main():
    n,k=map(int,input().split())
    g=[[] for i in range(50+ 1 )]
    for i in range(n):
        v,u=map(int,input().split())
        g[v].append(u)
        g[u].append(v)
    print(g)
for _ in range(int(input())):
   main()