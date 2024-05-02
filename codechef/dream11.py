import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    # print(a)
    # print(b)
    if n<4 or m<4:
        print(-1)
        return
    ans=sum(a[:4])
    ans+=sum(b[:4])
    rem=[]
    for i in range(4,n):
        rem.append(a[i])
    for i in range(4,m):
        rem.append(b[i])
    # print(rem)
    rem.sort(reverse=True)
    if len(rem)<3:
        print(-1)
        return
    for i in range(3):
        ans+=rem[i]
    print(ans)
for _ in range(int(input())):
   main()