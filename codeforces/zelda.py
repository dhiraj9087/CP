from collections import Counter
import math
import sys
input=sys.stdin.readline

def main():
    n=int(input())
    g = [[] for _ in range(n+1)]
    # g=[[] for i in range(n)]
    arr=[]
    for i in range(n-1):
        a,b=map(int,input().split())
        g[a].append(b)
        g[b].append(a)
        arr.append(a)
        arr.append(b)
    # print(g)
    # d=Counter(arr)
    ans=0
    # for i in d.values():
    #     if i>=3:
    #         ans+=1
    for i in g:
        if len(i)==1:
            ans+=1

    # if ans==0:
    #     print(1)
    #     return
    # if ans==1:
    #     print(2)
    #     return
    print(ans//2 + ans%2)

for _ in range(int(input())):
   main()