import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    s=list(s)
    if len(set(s))==1 and s[0]=='p':
        print("YES")
        return
    if len(set(s))==1 and s[0]=='.':
        print("YES")
        return
    if s[0]=='s':
        s[0]='.'
    if s[-1]=='p':
        s[-1]='.'
    flag1,flag2=False,False
    for i in range(n):
        if s[i]=='p':
            flag1=True
        elif s[i]=='s':
            flag2=True
    if flag1==True and flag2==True:
        print("NO")
        return
    print("YES")
    # rs=-1
    # rp=-1
    # for i in range(n):
    #     if s[i]=='s':
    #         rs=i
    #     elif s[i]=='p':
    #         rp=i
    # if rs>rp:
    #     print("NO")
    #     return
    # ind=-1
    # for i in range(rs,n):
    #     if s[i]=='p':
    #         ind=i
    #         break
    # if ind!=(n-1):
    #     print("NO")
    #     return
    # print("YES")
    # print(rs,rp,ind)
for _ in range(int(input())):
   main()