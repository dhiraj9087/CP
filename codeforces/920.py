import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    e,f=map(int,input().split())
    g,h=map(int,input().split())
    arr=[[a,b],[c,d],[e,f],[g,h]]
    arr.sort()
    # print(arr)
    print(abs(arr[0][1]-arr[1][1])*abs(arr[0][1]-arr[1][1]))

for _ in range(int(input())):
   main()