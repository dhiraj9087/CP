from collections import defaultdict
import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ca=list(map(int,input().split()))
    b=list(map(int,input().split()))
    cb=list(map(int,input().split()))
    vis=[[] for i in range(2*n+1)]
    for i,j in zip(a,ca):
        vis[j].append(i)
    for i,j in zip(b,cb):
        vis[j].append(i)
    for i in vis:
        i.sort(reverse=True)
    ind=0
    for i,j in zip(a,ca):
        if j not in cb:
            if i<ind:
                print("No")
                return
            ind=i
            continue
        while vis[j] and vis[j][-1]< ind:
            vis[j].pop()
        if not vis[j]:
            print("No")
            return
        ind = vis[j].pop()
    print("Yes")
for _ in range(int(input())):
   main()

