import math
import sys
input=sys.stdin.readline
mod=10**9 +7
def func(a, b):
    res = 1
    while b:
        if b & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        b >>= 1
    return res
def main():
    n=int(input())
    # print((1<<n)%mod)
    # ind=2**n
    # print(ind%mod)
    ans = 0
    last = 0
    
    for i in range(1, n + 1):
        ind = last
        ind = (ind * 2) % mod
        ind = (ind + ((i - 1) * (i - 1)) % mod) % mod
        ans = (ans + (ind * func(2, n - i)) % mod) % mod
        last = ind
    
    ans = (ans * 2) % mod
    print(ans)
for _ in range(int(input())):
   main()