import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    if n==3:
        print(0)
        return
    a.sort()
    # print(a)
    s1 = a[-3]-a[0]
    s2 = a[-1]-a[2]
    s3 = a[-2]-a[1]
    print(min(s1,s2,s3))

for _ in range(int(input())):
   main()