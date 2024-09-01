import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    c=0
    c2=0
    for i in range(n-1):
        if s[i]!=s[i+1]:
            c+=1
        else:
            c2+=1
    # print(c,c2)
    ans = c*c2
    ans+=(c*(c-1)//2)
    print(ans)    
for _ in range(int(input())):
   main()
