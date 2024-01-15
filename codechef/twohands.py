import math
import sys
input=sys.stdin.readline
def main():
   l,r,m=map(int,input().split())
   ans=math.ceil(m/l)+m//r
   print(ans)
for _ in range(int(input())):
   main()