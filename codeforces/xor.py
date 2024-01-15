import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    ans=[0]*n
    for i in range(1,n):
        ans[i]=ans[i-1]^a[i-1]
    print(*ans)
    for i in range(len(ans)):
        if ans[i]>=n-1:
            ans[i]=ans[i]%(n-1)
    print(*ans)
    print(2^5)
# for _ in range(int(input())):
main()