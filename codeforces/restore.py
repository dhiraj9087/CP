import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    b=list(map(int,input().split()))
    a=[b[0]]
    for i in range(n-2):
        a.append(min(b[i],b[i+1]))
    a.append(b[n-2])
    print(*a)
for _ in range(int(input())):
   main()
