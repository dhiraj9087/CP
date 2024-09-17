import math
import sys
input=sys.stdin.readline
from collections import deque
def bs(l,r,dq,num):
    while l<r:
        mid = (l+r)//2
        if dq[mid]<num:
            l = mid+1
        else:
            mid-1
    dq.insert(l,num)
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    dq = deque(a)
    add=0
    while k:
        mini = dq[0]
        maxi = dq[-1]
        num = mini+maxi
        dq.pop()
        dq.popleft()
        bs(0,len(dq),dq,num)
        k-=1
    print(*list(dq))
for _ in range(int(input())):
   main()