import math
import sys
input=sys.stdin.readline
from collections import *
def main():
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    # no=[]
    # d=Counter(b)
    # ans=""
    used = [False for i in range(n + 1)]
    for i in b:
        used[i] = True
    l = len(b)
    for i in range(m):
        if l == n or (l == n-1 and not used[a[i]]):
            print(1, end='')
        else:
            print(0, end='')
    print()
    # ans=""
    # for i in range(m):
    #     if d[a[i]]==1:
    #         ans+='1'
    #     else:
    #         ans+='0'
    # print(ans)

for _ in range(int(input())):
   main()