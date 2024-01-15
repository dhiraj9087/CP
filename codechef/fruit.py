import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d={}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]]=max(d[a[i]],b[i])
        else:
            d[a[i]]=b[i]
    add=0
    ans=float('-inf')
    for i in d.values():
        add+=i
        ans=max(ans,add)
    print(0 if ans<0 else ans)
for _ in range(int(input())):
   main()