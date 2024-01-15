import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    s=0
    ans=[]
    for i in range(n):
        a[i]+=s
        s=max(s,a[i])
        ans.append(a[i])
    print(*ans)
# for _ in range(int(input())):
main()