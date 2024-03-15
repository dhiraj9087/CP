import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    s=input().strip()
    if k==0:
        print(s)
        return
    one=s.count('1')
    ans=list(s)
    if one>k:
        for i in range(n):
            if ans[i]=='1' and k>0:
                ans[i]='0'
                k-=1
        print(''.join(ans))
        return
    print("0"*(n-k))
    # print(''.join(s))
for _ in range(int(input())):
   main()