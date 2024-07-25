import sys
input=sys.stdin.readline
def main():
    n,x,y=map(int,input().split())
    ans=[0]*(n+1)
    for i in range(y,x+1):
        ans[i]=1
    ind=-1
    for i in range(y-1,0,-1):
        ans[i]=ind
        ind = -ind
    ind=-1
    for i in range(x+1,n+1):
        ans[i]=ind
        ind = -ind
    ans=ans[1:]
    print(*ans)
for _ in range(int(input())):
   main()
