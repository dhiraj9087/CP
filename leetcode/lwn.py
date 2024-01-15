from collections import Counter
import math
import sys
input=sys.stdin.readline
def main():
    a = [1,3,2,3,3]
    k = 2
    # a = [1,4,2,1]
    # k = 3
    n=len(a)
    maxi=max(a)
    arr=[0]*n
    c=0
    for i in range(n):
        if a[i]==maxi:
            c+=1
            arr[i]=c
    print(arr)
    l,r=0,0
    ans=0
    while r<n:
        if arr[r]<k:
            r+=1
        ans+=1
        
        
    # return 4
# for _ in range(int(input())):
print(main())