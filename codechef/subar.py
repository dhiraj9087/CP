import math
import sys
from collections import defaultdict

input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    p=[0]*(n+1)
    # s=0
    for i in range(n):
        # s+=a[i]
        p[i+1]=a[i]+p[i]
    # p[0]=1
    # print(p)
    d=defaultdict(int)
    for i in range(n):
        for j in range(i+1,n+1):
            if p[j]-p[i]<=n:
                d[p[j]-p[i]]+=1
            else:
                break
    ans=[0]*(n+1)
    for i,j in d.items():
        ans[i]=j
    print(*ans[1:])
    # fib_sequence = [0, 1]
    # fib_sequence = [0, 1]
    # for i in range(2, n+1):
    #     fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    # print(*fib_sequence[1:n+1])
for _ in range(int(input())):
   main()