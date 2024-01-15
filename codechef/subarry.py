import math
import sys
input=sys.stdin.readline
def main():
   n=int(input())
   a=list(map(int,input().split()))
   ind=0
   if sorted(a)==a:
      print(0)
      return
   maxi = a[0]
   ans = 0
   for i in range(1, n):
      if a[i] < maxi:
         ans += 1
      else:
         maxi = a[i]
   
   print(ans)
for _ in range(int(input())):
   main()