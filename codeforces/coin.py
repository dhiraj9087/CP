import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    triangular_numbers = [1, 3, 6, 10, 15]
    coins_needed = 0

    # Greedily use the largest triangular number coins first
    for i in range(4, -1, -1):
        while n >= triangular_numbers[i]:
            n -= triangular_numbers[i]
            coins_needed += 1
    print(coins_needed)
for _ in range(int(input())):
   main()