import math
import sys
input=sys.stdin.readline
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes
MOD = 10**9 + 7
MAXN = 10**5 + 5

def get_primes():
    is_prime = [True] * (MAXN + 5)
    primes = []
    p_set = set()

    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(MAXN)) + 2):
        if is_prime[i]:
            primes.append(i * i)
            p_set.add(i * i)
            for j in range(i * i, MAXN, i):
                is_prime[j] = False

    for i in range(int(math.sqrt(MAXN)) + 3, MAXN):
        if is_prime[i]:
            primes.append(i * i)
            p_set.add(i * i)
    
    return primes, p_set
def main():
    n=int(input())
    a=4
    arr1,arr2=get_primes()
    # arr1=sieve_of_eratosthenes(MAXN)
    for b in arr1:
        c=n-a-b
        if c not in arr2:
            continue
        if a!=b and b!=c and c!=a and a+b+c==n:
            print("Yes")
            return
    print("No")
    # for p in primes:
    #     q_square = n - p**2
    #     if q_square < 0:
    #         break
    #     q = int(q_square**0.5)
    #     if q**2 == q_square and q in prime_set:
    #         print("Yes")
    #         return
    # print("No")
    # arr1,arr2=get_primes()
    # print(arr2)
for _ in range(int(input())):
   main()