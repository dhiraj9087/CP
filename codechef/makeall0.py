import math
import sys
from collections import Counter
input=sys.stdin.readline
def main():
    # n=int(input())
    # a=list(map(int,input().split()))
    # mini=min(a)
    n = int(input())
    l1 = list(map(int, input().split()))
    p = [l1[0]]
    for i in range(1,n):
        if l1[i] <= p[-1]:
            p.append(l1[i])
    print(p)
    ans = n
    x = n - len(p)
    for i in range(len(p)):
        ans = min(ans, p[i]+i+x)
    print(ans)
    # # ans=mini
    # if len(set(a))==1 and a[0]==1:
    #     print(1)
    #     return
    # if a[0]==1:
    #     a=[i-1 for i in a]
    #     ans=1
    #     ans+=sum(1 for i in a if i!=0)
    #     print(ans)
    #     return
    # # d=Counter(a)
    # d={}
    # for i in range(n):
    #     if a[i] in d:
    #         d[a[i]].append(i)
    #     else:
    #         d[a[i]]=[i]
    # print(d)
    # maxi=n+1
    # ans=n
    # for i,j in d.items():
    #     ind=j.index(maxi) if maxi in j else -1
    #     if ind>0:
    #         ind-=1
    #         n-=(ind+1)
    #         ans=min(ans,n+i)
    #         maxi=j[0]
    # print(ans)
    
    # d=[[a[i],i] for i in range(len(a))]
    # print(d)
    # d.sort()
    # print(d)
for _ in range(int(input())):
   main()