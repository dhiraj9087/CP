import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a,b=0,0
    bit=0
    while (1<<bit) <=n:
        bit+=1
    m=1<<(bit-1)
    print(n^m,m)
    
for _ in range(int(input())):
   main()