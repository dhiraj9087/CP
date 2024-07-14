import math
import sys
input=sys.stdin.readline
def main():
    n,m,k=map(int,input().split())
    ans=[]
    for i in range(n,k-1,-1):
        ans.append(i)
    for i in range(m+1,k):
        ans.append(i)
    for i in range(1,m+1):
        ans.append(i)
    print(*ans)
for _ in range(int(input())):
   main()




   