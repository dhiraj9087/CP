import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print(-1)
        return
    num=a[0]
    ans=n
    cur=0
    for i in range(n):
        if a[i]!=num:
            ans=min(ans,cur)
            cur=0
        else:
            cur+=1
    ans=min(ans,cur)
    print(-1 if ans==n else ans)
    # print(min(ans,ans2))
for _ in range(int(input())):
   main()