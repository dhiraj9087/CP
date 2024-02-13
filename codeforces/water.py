import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    mini=sum(a)//n
    maxi=0
    for i in range(n):
        if a[i]>mini:
            maxi+=abs(a[i]-mini)
        elif a[i]+maxi>=mini:
            maxi=a[i]+maxi-mini
        else:
            print("NO")
            return
            

    print("YES")
for _ in range(int(input())):
   main()