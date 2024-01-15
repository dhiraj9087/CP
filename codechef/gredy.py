import math
import sys
input=sys.stdin.readline
def main():
    n,x=map(int,input().split())
    a=[i for i in range(1,n+1)]
    if x==0:
        print(*a)
        return
    if n==x:
        print(-1)
        return
    if n-x<=1:
        print(-1)
        return
    ans=[x+2]
    c=1
    for i in range(1,n):
        if i==(x+2):
            c+=1
        ans.append(c)
        c+=1
    print(*ans)
    # k=x+1
    # ans=[]
    # for i in range(n,k+2,-1):
    #     ans.append(i)
    # for i in range(1,k+1):
    #     ans.append(i)
    # print(ans)
for _ in range(int(input())):
   main()