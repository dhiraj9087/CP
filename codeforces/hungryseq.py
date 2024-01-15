import math
import sys
input=sys.stdin.readline
mod=10000000

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
    ans=[2]
    ind=3
    while len(ans)<n:
        if isPrime(ind):
            ans.append(ind)
        ind+=2
    print(*ans)
# for _ in range(int(input())):
main()