import math
import sys
input=sys.stdin.readline
def main():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=a[0]
    mini=maxi=a[0]
    for i in a[1:]:
        x^=i
    # print(x)
    for j in b:
        new=x
        for k in range(len(a)):
            a[i]=a[i]|j
            new^=a[i]
        mini=min(mini,new)
        maxi=max(maxi,new)
    print(mini,maxi)
        
for _ in range(int(input())):
   main()