import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    a,b=0,0
    ans=0
    for i in range(n):
        if s[i]=='?':
            a+=1
        else:
            b+=(int(s[i]))
    if s[0]=='?':
        print('1'+'0'*(a-1))
        return
    if a>0:
        b=b%9
        if b==0:
            print('1'*(a-1)+'2')
            return
        print('1'*a)
        return
    else:
        if b%9==0:
            print(0)
            return
        print(1)
        return
for _ in range(int(input())):
   main()