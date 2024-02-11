import math
import sys
input=sys.stdin.readline
lim=100
def main():
    n,x=map(int,input().split())
    ans=0
    for i in range(n):
        k=i
        r=k-2
        r_ind=k-r
        s=k+(k-2)
        if r_ind==n or s%n==x:
            ans+=1
    print(ans)
for _ in range(int(input())):
   main()