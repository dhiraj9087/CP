import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    pair=0
    ans=0
    for i in range(n):
        if a[i]==1:
            ans+=n
            continue
        for j in range(n):
            op = a[i]**(j+1)
            # if op>1000000007:
            #     break
            if op <= a[j]:
                ans+=1
    print(ans)
for _ in range(int(input())):
   main()