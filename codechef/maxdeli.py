import math
import sys
input=sys.stdin.readline
def main():
    n,k,l=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    # print(a)
    ans=0
    for i in range(l-1,n,k):
        ans+=a[i]
    print(ans)
for _ in range(int(input())):
   main()