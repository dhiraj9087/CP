import math
import sys
input=sys.stdin.readline

def main():
    n=int(input())
    a=list(map(int,input().split()))
    a2=a.copy()
    a2.sort(reverse=True)
    d={}
    for i in range(n):
        d[a2[i]]=i+1
    arr=[]
    for i in range(n):
        arr.append(d[a[i]])
    # print(arr)
    diff=0
    for i in range(n-1):
        if abs(arr[i]-arr[i+1])==1:
            diff+=1
    print(n-diff)
    # print(l)
for _ in range(int(input())):
   main()