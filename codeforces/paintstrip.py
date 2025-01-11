import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    num=1
    ans=1
    while True:
        if num>=n:
            print(ans)
            return
        ans+=1
        num = num*2+2
for _ in range(int(input())):
   main()