import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    ans=[]
    for i in range(62,-1,-1):
        x=1<<i
        if (x&n)==x and x!=n:
            ans.append(n-x)
    ans.append(n)
    print(len(ans))
    print(*ans)
for _ in range(int(input())):
   main()