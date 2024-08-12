import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=[i for i in range(1,n+1)]
    mid=(n+1)//2
    h1=a[:mid]
    h2=a[mid:]
    ans=[]
    for i in range(len(h2)):
        ans.append(h1[i])
        ans.append(h2[i])
    if len(h1)>len(h2):
        ans.append(h1[-1])
    print(*ans)
for _ in range(int(input())):
   main()