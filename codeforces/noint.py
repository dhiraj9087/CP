import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    d={1:[],2:[],3:[]}
    mini=float('-inf')
    maxi=float('inf')
    for i in range(n):
        a,b=map(int,input().split())
        d[a].append(b)
        if a==1:
            mini=max(mini,b)
        if a==2:
            maxi=min(maxi,b)
    # print(d,mini,maxi)
    if mini>maxi:
        print(0)
        return
    # arr=[i for i in range(mini,maxi+1)]
    ans=maxi-mini+1
    for i in range(len(d[3])):
        if d[3][i]>=mini and d[3][i]<=maxi:
            ans-=1
    print(ans)
    # print(len(arr))
for _ in range(int(input())):
   main()