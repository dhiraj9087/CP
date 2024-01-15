import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    print("First" if n%3!=0 else "Second")
for _ in range(int(input())):
   main()