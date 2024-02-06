import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    q=int(input())
    pre=[0]*n
    pre[n-1]=n
    for i in range(n - 2, -1, -1):
            if a[i]==a[i+1]:
                pre[i]=pre[i+1]
            else:
                pre[i]=i+1
    for i in range(q):
        ans=[]
        x,y=map(int,input().split())
        if pre[x-1]>y-1:
            ans.append([-1,-1])
        else:
            ans.append([x,pre[x-1]+1])
        for j,k in ans:
            print(j,k)
    print()

for _ in range(int(input())):
   main()

