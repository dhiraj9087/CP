import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    pair=[[a[2*n-i-1],a[i]] for i in range(n)]
    # print(pair)
    ans=0
    for i in range(len(pair)-1):
        ans+=((abs(pair[i][0]-pair[i+1][0]))+abs(pair[i][1]-pair[i+1][1]))
    print(ans)
    for i in range(len(pair)):
        print(pair[i][0],pair[i][1])
    
for _ in range(int(input())):
   main()