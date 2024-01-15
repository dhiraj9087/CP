import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    h=list(map(int,input().split()))
    maxi=curr=add=0
    ind=0
    for i in range(n):
        while ind<n and (add+a[ind]<=k) and (h[i]%h[ind]==0):
            add+=h[ind]
            curr+=1
            ind+=1
        if curr>maxi:
            maxi=curr
        if ind > i:
            add -= a[i]
            curr -= 1
    print(maxi)
for _ in range(int(input())):
   main()