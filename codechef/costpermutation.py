import math
import sys
input=sys.stdin.readline
from heapq import heappush, heappop

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a=[x-1 for x in a]
    vis=[False]*n
    cycle_lengths=[]
    for i in range(n):
        if not vis[i]:
            cycle_len=0
            curr=i
            while not vis[curr]:
                vis[curr]=True
                curr=a[curr]
                cycle_len+=1
            cycle_lengths.append(cycle_len)
    pq=cycle_lengths[:]
    pq.sort()
    ans=0
    while len(pq)>1:
        l1=heappop(pq)
        l2 = heappop(pq)
        ans += (l1+l2)
        heappush(pq,l1+l2)
    print(ans)
for _ in range(int(input())):
   main()