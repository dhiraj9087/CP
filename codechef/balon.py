import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=list(map(int,input().split()))
    print("YES" if a.count(2) % 8==0 else "NO")
    # print(math.pow(pro,1/8)) 
for _ in range(int(input())):
   main()