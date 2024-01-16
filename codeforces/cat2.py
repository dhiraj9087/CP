import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=input().strip()
    b=input().strip()
    if a==b:
        print(0)
        return
    c1,c2=0,0
    for i in range(n):
        if a[i]=='1' and b[i]=='0':
            c1+=1
        if a[i]=='0' and b[i]=='1':
            c2+=1
    print(max(c1,c2))


for _ in range(int(input())):
   main()