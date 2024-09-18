import math
import sys
input=sys.stdin.readline

def main():
    n=int(input())
    s=input().strip()
    n = int(math.sqrt(n))
    one = s.count('1')
    if (n*4 - 4 )!= one:
        print("No")
        return
    zero = s.count('0')
    if (n*n-(n*4 - 4 ))!=zero:
        print("No")
        return
    print("Yes")
for _ in range(int(input())):
   main()