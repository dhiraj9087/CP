import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    maxi=float('-inf')
    y=-1
    for i in range(1,n):
        if math.gcd(n,i) + i >maxi:
            maxi=math.gcd(n,i)+i
            y=i
    print(y)
for _ in range(int(input())):
   main()