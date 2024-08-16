import math
import sys
input=sys.stdin.readline
def main(arr):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in range(n):
        ele = a[i]
        for j in range(ele+1,201):
            if arr[j]==False:
                diff = abs(a[i]-j)
                if diff in d:
                    print(i+1,d[diff]+1)
                    return
        d[ele]=i
    print(-1)


def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime
for _ in range(int(input())):
   arr=sieve_of_eratosthenes(201)
   main(arr)