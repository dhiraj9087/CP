import math
import sys
input=sys.stdin.readline
def sieve_of_eratosthenes(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [i for i in range(n+1) if primes[i]]
def main():
    l,r=map(int,input().split())
    arr1=[i for i in range(l,r+1)]
    # ans=[i+1 for i in range(l,r+1)]
    ans=[]
    # if math.gcd(arr1[0],arr1[-1])==1:
    #     ans[-1]=arr1[0]
    #     print(*ans)
    #     return
    # s=set(ans)
    # a=sieve_of_eratosthenes(r+1)
    # p=[i for i in a if i >= l]
    # print(p)
    # for i in range(len(p)):
    #     if math.gcd(arr1[-1],p[i])==1 and (p[i] not in s):
    #         ans[-1]=p[i]
    #         print(*ans)
    #         return
    # print(-1)
    if (r-l+1)%2==0:
        for i in range(l,r+1,2):
            ans.append(i)
        print(*ans)
        return
    
for _ in range(int(input())):
   main()
import math

def main():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        if math.gcd(l, r) == 1:
            for i in range(l + 1, r + 1):
                print(i, end=" ")
            print(l)
        elif (r - l + 1) % 2 == 0:
            for i in range(l, r + 1, 2):
                print(i + 1, i, end=" ")
        elif l % 2 != 0 and r % 2 != 0:
            print(l + 1, l + 2, l, end=" ")
            for i in range(l + 3, r + 1, 2):
                print(i + 1, i, end=" ")
        else:
            print(-1)
        print()

if __name__ == "__main__":
    main()
