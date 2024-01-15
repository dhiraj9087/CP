import math
import sys
input=sys.stdin.readline
def isalter(a):
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            return False
    return True
def main():
    n,m=map(int,input().split())
    s=input().strip()
    t=input().strip()
    if isalter(s)==True:
        print("Yes")
        return
    if isalter(t)==False:
        print("No")
        return
    ans=""
    for i in range(len(s)):
        ans+=s[i]
        if i<len(s)-1 and s[i]==s[i+1]:
            ans+=t
    # print(ans)
    # if n==1:
    #     print("Yes")
    #     return
    # if n==2 and len(set(s))==2:
    #     print("Yes")
    #     return
    # l=0
    # while l<len(s):
    #     if s[l]==s[l+1]:
    #         s=s[:l+1]+t+s[l+1:]
    #         l=l+m

    # for i in range(n-1):
    #     if s[i]==s[i+1]:
    #         s=s[:i+1]+t+s[i+1:]
    for i in range(len(ans)-1):
        if ans[i]==ans[i+1]:
            print("No")
            return
    print("Yes")
   
    # print(s)
for _ in range(int(input())):
   main()