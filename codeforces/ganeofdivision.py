import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=[]
    for i in range(n):
        ind=i
        for j in range(n):
            if j!=ind:
                if abs(a[i]-a[j])%k==0:
                    l.append(i)
    if len(set(l))==n:
        print("NO")
        return
    for i in range(n):
        if i not in l:
            print("YES")
            print(i+1)
            return
for _ in range(int(input())):
   main()