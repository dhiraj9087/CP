import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    if n==1 or n==2:
        print("Bob")
        return
    if n%2==0:
        print("Bob")
        return
    print("Alice")
for _ in range(int(input())):
   main()