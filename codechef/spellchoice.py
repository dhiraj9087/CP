import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=[]
    for i in range(n):
        x,y=map(int,input().split())
        a.append([x,y])
    ans=float('-inf')
    for i in range(len(a)):
        for j in range(i+1,len(a)):

            ans=max(ans,a[i][0]*a[j][1] + a[i][1]*a[j][0])
    print(ans)

for _ in range(int(input())):
   main()