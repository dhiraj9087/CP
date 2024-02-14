N = 10**6
is_prime = [True] * N
prime_numbers = []

def sieve():
    is_prime[0] = is_prime[1] = False
    for i in range(2, N):
        if is_prime[i]:
            for j in range(2*i, N, i):
                is_prime[j] = False

def solve():
    n = int(input())
    if n % 2:
        print(1, end=" ")
        for i in range(n // 2):
            print(prime_numbers[i], prime_numbers[i], end=" ")
        print()
    else:
        for i in range(n // 2):
            print(prime_numbers[i], prime_numbers[i], end=" ")
        print()

def main():
    t = int(input())
    sieve()

    for i in range(N):
        if is_prime[i]:
            prime_numbers.append(i)

    while t > 0:
        solve()
        t -= 1

if __name__ == "__main__":
    main()
