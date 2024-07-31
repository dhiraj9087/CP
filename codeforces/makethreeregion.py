import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s1=input().strip()
    s2=input().strip()
    ans=0
    for i in range(n-2):
        if s1[i]=='x' and s1[i+1]=='.' and s1[i+2]=='x' and s2[i]=='.' and s2[i+1]=='.' and s2[i+2]=='.':
            ans+=1
    for i in range(n-2):
        if s2[i]=='x' and s2[i+1]=='.' and s2[i+2]=='x' and s1[i]=='.' and s1[i+1]=='.' and s1[i+2]=='.':
            ans+=1
    print(ans)
for _ in range(int(input())):
   main()