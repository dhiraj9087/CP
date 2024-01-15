import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    # if sum(a)!=sum(b):
    #     print("NO")
    #     return
    a.sort()
    b.sort(reverse=True)
    c=[]
    for i in range(n):
        c.append(a[i]+b[i])
    # print(c)
    if len(set(c))!=1:
        print(-1)
        return
    print(*a)
    print(*b)
for _ in range(int(input())):
   main()