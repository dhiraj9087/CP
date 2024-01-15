import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=[0]*n
    ans[0]=a[0]
    ind=a[0]
    for i in range(1,n):
        ans[i] = ans[i]&ans[i-1]
    print(ans)

    q=int(input())
    for i in range(q):
        l,r=map(int,input().split())

for _ in range(int(input())):
   main()