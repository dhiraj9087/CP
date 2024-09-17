import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=[]
    for i in range(n):
        s=input().strip()
        a.append(s)
    ans=[]
    for i in range(n):
        ind = a[i].find('#')
        ans.append(ind+1)
    ans=ans[::-1]
    print(*ans)
for _ in range(int(input())):
   main()