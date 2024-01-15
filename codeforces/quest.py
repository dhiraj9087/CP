import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ans,maxi,bmaxi=0,0,0
    for i in range(n):
        if i==k:
            break
        maxi+=a[i]
        bmaxi=max(bmaxi,b[i])
        ans=max(maxi+(k-i-1)*bmaxi,ans)
    print(ans)
for _ in range(int(input())):
   main()