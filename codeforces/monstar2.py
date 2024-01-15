import math
import sys
input=sys.stdin.readline
def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    n=int(input())
    ans=0
    p=1
    while n>0:
        if n>0 and isPrime(n):
            print(ans+1)
            return
        n-=p
        p=p*2
        ans+=1
    if n!=0:
        print(-1)
        return
    print(ans)
for _ in range(int(input())):
   main()