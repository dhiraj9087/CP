import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    # if n==1:
    #     print(1)
    #     return
    d=[]
    for i,j in enumerate(a):
        d.append([j,i])
    d.sort()
    # print(d)
    m={}
    ind=n
    for i in range(n):
        m[d[i][1]]=ind
        ind-=1
    # print(m)
    ans=[]
    for i in range(n):
        ans.append(m[i])
    print(*ans)


for _ in range(int(input())):
   main()