import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if n == 1:
        if a[0] == 0 and a[1]==0:
            print(0,0)
            return
        if a[0]==1 and a[1]==1:
            print(0,0)
            return
        print(1,1)
        return
    one,zero = a.count(1),a.count(0)
    mini,maxi = float('inf'),float('-inf')
    if one%2==0 and zero%2==0:
        mini = 0
        maxi = min(one,zero)
        print(mini,maxi)
        return
    if one%2==1 and zero%2==1:
        mini = 1
        maxi = min(one,zero)
        print(mini,maxi)
        return
    
for _ in range(int(input())):
   main()