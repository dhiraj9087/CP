import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    s=input().strip()
    ans=0
    d={'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0}
    for i in s:
        d[i]+=1
    ans=0
    for i,j in d.items():
        if j<m:
            ans+=(m-j)
    print(ans)
for _ in range(int(input())):
   main()