import math
import sys
input=sys.stdin.readline
def is_square_of_odd(n):
    if n < 0:
        return False  
    root = int(n**0.5)  
    return root * root == n and root % 2 == 1 

def main():
    n=int(input())
    a=list(map(int,input().split()))
    l=[1,9,25,49,81]
    add=0
    ans=0
    for i in range(n):
        add+=a[i]
        if is_square_of_odd(add):
            ans+=1
    print(ans)
for _ in range(int(input())):
   main()