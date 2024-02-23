import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ind1,ind2=-1,-1
    for i in range(n):
        if a[i]==1:
            ind1=i
            break
    for i in range(n-1,-1,-1):
        if a[i]==1:
            ind2=i
            break
    # print(ind1,ind2)
    if ind1==-1 or ind2==-1:
        print(0)
        return
    if len(set(a))==1 and a[0]==1:
        print(0)
        return
    ans=0
    for i in range(ind1,ind2):
        # print(a[i])
        if a[i]==0:
            ans+=1
    print(ans)
for _ in range(int(input())):
   main()