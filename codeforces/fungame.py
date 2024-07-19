import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    t=input().strip()
    c=0
    for i in range(n):
        if s[i]=='0'and t[i]!='0' and c==0:
            print("NO")
            return
        if s[i]=='1':
            c+=1
    print("YES")
    # if s==t:
    #     print("YES")
    #     return
    # if n==1:
    #     if s=='0' and t=='1':
    #         print("NO")
    #         return
    # if s[0]=='1':
    #     print("YES")
    #     return
    # ind_s,ind_t=-1,-1
    # for i in range(n):
    #     if s[i]=='1':
    #         ind_s=i
    #         break
    # for i in range(n):
    #     if t[i]=='1':
    #         ind_t=i
    #         break
    # if ind_s>ind_t:
    #     print("NO")
    #     return
    # print("YES")
for _ in range(int(input())):
   main()