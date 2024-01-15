import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    maxi=math.gcd(*a)
    var=0
    for i in range(n):
        var=a[i]
        a[i]=b[i]
        maxi=max(maxi,math.gcd(*a))
        a[i]=var
        # print(maxi,a)

    print(maxi)
    a='abcdefghijklmnopqrstuvwxyz'
    print(len(a))

for _ in range(int(input())):
   main()