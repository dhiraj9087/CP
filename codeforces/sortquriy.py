import math
import sys
input=sys.stdin.readline
from collections import Counter
def main():
    n,k=map(int,input().split())
    a=input().strip()
    b=input().strip()
    arr1=[[0]*n for i in range(26)]
    arr2=[[0]*n for i in range(26)]
    for i in range(n):
        arr1[ord(a[i])-ord('a')][i]+=1
        arr2[ord(b[i])-ord('a')][i]+=1
    for i in range(26):
        for j in range(1,n):
            arr1[i][j] += arr1[i][j-1]
            arr2[i][j] += arr2[i][j-1]

    for i in range(k):
        l,r=map(int,input().split())
        l-=1
        r-=1
        c=0
        ans=0
        for j in range(26):
            ca = arr1[j][r]
            cb=arr2[j][r]
            if l>0:
                ca = ca - arr1[j][l-1]
                cb = cb - arr2[j][l-1]
            ans += abs(ca-cb)

        c += ans//2
        print(c)
        
for _ in range(int(input())):
   main()