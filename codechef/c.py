# def minimum_time_to_reach_score(X, Y):
#     """
#     This function takes two integers X and Y as input and returns the minimum time in seconds for Chef's score
#     to become greater than or equal to Y, given that Chef starts with a score of X and adds the smallest prime
#     factor of his score every second.
#     """
#     score = X
#     time = 0
#     while score < Y:
#         # Find the smallest prime factor of the current score
#         smallest_prime_factor = None
#         for i in range(2, int(score ** 0.5) + 1):
#             if score % i == 0:
#                 smallest_prime_factor = i
#                 break
#         if smallest_prime_factor is None:
#             # If the current score is prime, add the score itself as the smallest prime factor
#             smallest_prime_factor = score
#         # Add the smallest prime factor to the score and increment the time
#         score += smallest_prime_factor
#         time += 1
#     return time

# # Example usage
# print(minimum_time_to_reach_score(5,100))
print(20%8)