import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    flag=False
    c=1
    for i in range(1,n):
        if a[i]>a[i-1]:
            c+=1
            
    if c!=n:
        ans=0
        maxi=float('-inf')
        for i in range(n-1):
            if a[i]<=a[i+1]:
                ans+=1
            else:
                ans=1
            maxi=max(maxi,ans)
        print(maxi)
    else:
        print(0)
for _ in range(int(input())):
   main()