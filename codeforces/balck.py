import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    l,r=s.find('B'),s.rfind('B')
    print(r-l+1)
for _ in range(int(input())):
   main()