import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    pair1,pair2=0,0
    if n==1:
        print("YES")
        return
    if n==2:
        if len(set(s))==1:
            print("NO")
            return
        print("YES")
        return
    for i in range(n-1,-1,-1):
        if s[i]=='0':
            pair1+=1
        else:
            pair1-=1
        if pair1<-1 or pair1>1:
            print("NO")
            return
    print("YES")
    # print(a)
    # if '0' not in s:
    #     print("Yes")
    # elif s.startswith('1') and s.rstrip('1') == '0':
    #     print("Yes")
    # elif s.endswith('1') and s.lstrip('1') == '0':
    #     print("Yes")
    # else:
    #     print("No")

    # one,zero=0,0
    # for i in range(n):
    #     if s[i]=='1':
    #         one=i
    # for i in range(n):
    #     if s[i]=='0':
    #         zero=i
    # print(one,zero)
    # for i in range(one+1,n):
    #     if s[i]=='0':
    #         print("NO")
    #         return
    # for i in range(zero+1,n):
    #     if s[i]=='1':
    #         print("NO")
    #         return
    # print("YES")
    # for i in range(0,n,2):
    #     if i+1<n:
    #         if s[i]=='1' and s[i+1]=='0':
    #             pair1+=1
    #         if s[i]=='0' and s[i+1]=='1':
    #             pair2+=1
    # if n%2==0 and (pair1*2==n or pair2*2==n):
    #     print("YES")
    #     return
    # print("NO")
    # print(pair1,pair2)
for _ in range(int(input())):
   main()