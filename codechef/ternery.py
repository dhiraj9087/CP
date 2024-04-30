import math
import sys
input=sys.stdin.readline
def to_ternary(decimal):
    ternary_digits = []
    while decimal > 0:
        quotient, remainder = divmod(decimal, 3)
        ternary_digits.append(remainder)
        decimal = quotient
    
    if not ternary_digits:  # Handle the case when the input is 0
        ternary_digits.append(0)
    
    ternary_digits.reverse()
    return "".join(map(str, ternary_digits))
def has_digit_2_in_ternary(decimal):
    while decimal > 0:
        if decimal % 3 == 2:
            return True
        decimal //= 3
    return False
def main():
    n=int(input())
    for i in range(1,11):
        print((to_ternary(i),bin(i)[2:]),end=' ')
    print()
for _ in range(int(input())):
   main()




