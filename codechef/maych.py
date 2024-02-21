import math
import sys
input=sys.stdin.readline
def main():
    ans=[]
    for i in range(1,23):
        a,b=map(int,input().split())
        ans.append([a+b*20 , i])
    ans.sort()
    print(ans[-1][1])
for _ in range(int(input())):
   main()