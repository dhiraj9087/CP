# # def palin(s):
# #     freq = {}
# #     for c in s:
# #         if c in freq:
# #             freq[c] += 1
# #         else:
# #             freq[c] = 1

# #     odd_count = 0
# #     for count in freq.values():
# #         if count % 2 != 0:
# #             odd_count += 1
# #         if odd_count > 1:
# #             return False

# #     return True



# def solve():
#     n=int(input())
#     s=input()
#     freq = {}
#     for c in s:
#         if c in freq:
#             freq[c] += 1
#         else:
#             freq[c] = 1

#     odd_count = 0
#     for count in freq.values():
#         if count % 2 != 0:
#             odd_count += 1
#     if n % 2 == 1:
#         if odd_count > 1:
#             return n - odd_count + 1
#         else:
#             return n - 1
#     else:
#         if odd_count > 0:
#             return n - odd_count
#         else:
#             return n - 2
#     # if not palin(s):
#     #     print(0)
#     # else:
#     #     for i in range(n):
#     #         s[i]=

# for _ in range((int(input()))):
#     print(solve())
def solve():
    n = int(input())
    s = input()
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    odd_count = 0
    for count in freq.values():
        if count % 2 != 0:
            odd_count += 1

    
    if len(freq) == 1:
        if n % 2 == 0:
            print(1)
        else:
            print(2)
    else:
        if odd_count > 1:
            print(0)
        else:
            print(1)

for _ in range((int(input()))):
    solve()
