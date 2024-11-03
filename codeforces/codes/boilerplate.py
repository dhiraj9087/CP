import math
import sys
input=sys.stdin.readline
def countDigit(n):
    if n == 0:
        return 1
    count = 0
    while n != 0:
        n = n // 10
        count += 1
    return count

def checkPalindromenumber(n):
    reverse = 0
    temp = n
    while temp != 0:
        reverse = (reverse * 10) + (temp % 10)
        temp = temp // 10
    return reverse == n

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def findTrailingZeros(n):
    if n < 0:  
        return -1
    count = 0
    i = 5
    while n // i >= 1:
        count += n // i
        i *= 5
    return count

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a // gcd(a, b)) * b

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

def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def printPrimeFactors(n):
    
    if n <= 1:
        return
    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2

    while n % 3 == 0:
        print(3, end=" ")
        n = n // 3
    i = 5
    while i * i <= n:
        while n % i == 0:
            print(i, end=" ")
            n = n // i
        while n % (i + 2) == 0:
            print(i + 2, end=" ")
            n = n // (i + 2)
        i += 6
    if n > 3:
        print(n, end=" ")
    print()

def printDivisors(n):
    a=[]
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if n // i == i:
                a.append(i)
            else:
                a.append(i)
                a.append(n//i)
    return a

def power(x, y):
    if y == 0:
        return 1
    temp = power(x, y // 2)
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp

def isKthBitSet(n, k):
    if n & (1 << (k - 1)):
        return True
    else:
        return False


# def ispowof2(n):
#     if n==0:
#         return False
#     while n!=1:
#         if n%2!=0:
#             return False
#         n=n//2
#     return True


def isPowerofTwo(n):
    return n != 0 and (n & (n - 1)) == 0

def binary_search(arr, target,left,right):
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1