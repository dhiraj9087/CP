import math
import sys
input=sys.stdin.readline
def main():
    x,y,z=map(int,input().split())
    a=[x,y,z]
    for i in range(5):
        a.sort()
        a[0]+=1
    print(a[0]*a[1]*a[2])
for _ in range(int(input())):
   main()