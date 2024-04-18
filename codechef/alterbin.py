import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    if n==1:
        print(0)
        return
    if n==2:
        print(1 if len(set(s))==1 else 0)
        return
    c=0
    for i in range(n-1):
        if s[i]==s[i+1]:
            c+=1
    print(c)
for _ in range(int(input())):
   main()