import math
import sys
input=sys.stdin.readline
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num

def isfactor(Y,X):
    # valid = True
    i = 2
    while i * i <= Y:
        if Y % i == 0:
            if i < X or (Y // i) < X:
                return False
        i += 1
    return True
def is_valid_y(y, x):
    if is_prime(y) or is_perfect_square(y):
        return False
    if isfactor(y,x):
        return False
    return True
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while not is_prime(n):
        n += 1
    return n
def main():
    n = int(input())
    p1 = next_prime(n)
    p2 = next_prime(p1 + 1)
    print(p1 * p2)
for _ in range(int(input())):
   main()