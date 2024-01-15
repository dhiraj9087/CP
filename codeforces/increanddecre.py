import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    mid=sum(a)//2
    ans=0
    for i in range(n-1):
        if a[i]==mid:
            ans+=1
        elif a[i]>mid:
            a[i+1]+=(a[i]-mid)
            a[i]=mid
            ans+=1
        else:
            a[i+1]-=(-a[i]+mid)
            a[i]=mid
            ans+=1
    if a[n-1]==mid:
        ans+=1
    print(ans)
# for _ in range(int(input())):
main()