import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    b=bin(n)[2:]
    ans=0
    for i in b:
        ans+=(int(i))
    print("EVEN" if ans%2==0 else "ODD")
for _ in range(int(input())):
   main()