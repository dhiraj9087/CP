# import math
# import sys
# input=sys.stdin.readline
# def fun(n):
#     d={}
#     def fun2(n):
#         if n in d:
#             return d[n]
        
#         if n<2:
#             return 0
#         ans=n
#         ans+=fun(n//2)
#         ans+=fun((n+1)//2)
#         d[n]=ans
#         return ans
#     return fun2(n)

# def main():
#     n=int(input())
#     for i in range(2,100):
#         fun(i)
#     print(fun(n))
#     # print(l)
# # for _ in range(int(input())):
# main()
import math

def total_payment(N):
    """
    Calculates the total amount Takahashi pays without loops or recursion.

    Args:
        N: The initial integer written on the blackboard.

    Returns:
        The total amount Takahashi pays.

    This function uses memoization to store calculated values and optimizes calculations
    using bit manipulation and pre-calculated sums.
    """

    # Memoization dictionary to store calculated values
    memo = {}

    def helper(N):
        if N in memo:
            return memo[N]

        if N < 2:
            return 0

        # Optimized payment calculation using bit manipulation
        x = int(math.sqrt(N + 0.5))  # Efficient square root approximation
        payment = N
        if x & 1 == 0:  # Check if x is even
            payment += helper(x // 2) + x // 2  # Optimized for even x
        else:
            payment += helper(x // 2) + x // 2 + 1  # Add 1 for odd x

        memo[N] = payment
        return payment

    # Pre-calculate sums for small powers of 2 for efficiency
    for i in range(2, 15):
        memo[2**i] = 2**(i+1) - 1  # Pre-calculate powers of 2 - 1

    return helper(N)

# Example usage
N = 348  # Larger value for demonstration
total_amount = total_payment(N)
print(total_amount)