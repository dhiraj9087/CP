import math
import sys
input=sys.stdin.readline
def main():
    n, k, x = map(int, input().split())
    add = n*(n+1)//2
    add2 = k*(k+1)//2
    a = n-k
    add3 = a*(a+1)//2
    add4 = add-add3
    if add2 <= x and add4 >= x:
        print("YES")
    else:
        print("NO")
        
    
for _ in range(int(input())):
   main()