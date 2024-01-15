import math
import sys
input=sys.stdin.readline
def main():
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    x=list(map(int,input().split()))
    maxi=max(x)
    mini=min(x)
    count = [0] * (maxi + 1)
    p=[]
    p2=[]
    q=set()
    for i in x:
        if i not in q:
            q.add(i)
            p2.append(i)
    # print(p2)
    for i in range(len(p2)):
        p.append(2**p2[i])
    # print(p)
    for i in range(len(p)):
        for j in range(n):
            if a[j]%p[i]==0:
                d=int(math.log2(p[i]))
                a[j]+=((2**(d-1)))
    print(*a)
for _ in range(int(input())):
   main()