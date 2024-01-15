import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    maxi=float('-inf')
    l,r=0,0
    while r<n:
        if a[r]==0:
            c+=1
        while c>k:
            if a[l]!=1:
                c-=1
            l+=1
        maxi=max(maxi,r-l+1)
        r+=1    
    print(maxi)
# for _ in range(int(input())):
main()