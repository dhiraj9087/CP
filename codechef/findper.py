import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    pos=[0]*(n+1)
    ans=[]
    for i in range(len(a)):
        if not pos[a[i]]:
            ans.append(a[i])
        pos[a[i]]=1
    print(*ans)
for _ in range(int(input())):
   main()