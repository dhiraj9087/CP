import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if len(set(a))==1:
        print("Yes")
        return
    if len(set(a))>2:
        print("No")
        return
    d={}
    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i,j in d.items():
        if j>(n+1)//2:
            print("No")
            return
    print("Yes")
for _ in range(int(input())):
   main()