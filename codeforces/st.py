import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    s=input()
    t=input()
    if n==1:
        print("Yes")
        return
    if n==2 and len(set(s))==2:
        print("Yes")
        return
    for i in range(n-1):
        if s[i]==s[i+1]:
            s=s[:i+1]+t+s[i+1:]
    for i in range(len(s)):
        if s[i]==s[i+1]:
            print("No")
            return
    # print("Yes")
    print(s)
    # print(s)
for _ in range(int(input())):
   main()