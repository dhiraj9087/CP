import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    if (a+b) %2==1:
        print("Alice")
        return
    print("Bob")
for _ in range(int(input())):
   main()