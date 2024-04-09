import math
import sys
input=sys.stdin.readline
def main():
    n,k=map(int,input().split())
    rem=n//k
    c=0
    while c<k:
        c+=1
        print(rem,end=' ')
        rem+= n//k
    print()
for _ in range(int(input())):
   main()