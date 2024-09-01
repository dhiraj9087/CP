import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    ans=[]
    maxi=max(a)
    for _ in range(m):
        c,l,r = map(str,input().split())
        l,r=int(l),int(r)
        if l<=maxi<=r:
            if c=="-":
                maxi-=1
            else:
                maxi+=1
        ans.append(maxi)
    print(*ans)
for _ in range(int(input())):
   main()