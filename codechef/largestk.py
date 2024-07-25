import math
import sys
input=sys.stdin.readline
from collections import Counter

def main():
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==n:
        print(n)
        return
    d=Counter(a)
    d2 = sorted(d.items(),key=lambda x:x[1], reverse=True)
    ans=0
    arr=[0]*(len(d2)+1)
    for i in range(len(d2)):
        arr[i+1] = arr[i] + d2[i][1]
    
    for i in range(1,min(len(d2)+1,n+1)):
        k = (arr[i]//i)*i
        ans=max(ans,k)
    print(ans)
for _ in range(int(input())):
   main()