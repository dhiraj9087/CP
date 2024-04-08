import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    maxi=float('-inf')
    for i in range(n-1):
        maxi=max(maxi,abs(a[i]-a[i-1]))
    # print(maxi)
    ind=[]
    for i in range(1,n):
        if a[i]<a[i-1]:
            a[i]+=maxi
            ind.append([i,i-1])
    print(ind)
    if sorted(a)==a:
        print("Yes")
        return
    print("No")
for _ in range(int(input())):
   main()