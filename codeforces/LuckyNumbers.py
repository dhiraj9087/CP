# for i in range((int(input()))):
#     a,b=map(int,input().split())
#     q,m=[],[]
#     for i in range(a,b+1):
#         q.append(str(i))
#         s=[]
#         max_index,max_value=0,0
#         for j in (str(i)):
#             s.append(int(j))
#         # m.append(max(s)-min(s))
#             dif=max(s)-min(s)
#             if dif>max_value:
#                 max_value=dif
#                 max_index=i
#     print(max_index)


    # d=max(m)
    # z=m.index(d)
    # for i in range(len(m)):
    #     if m[i]==d:
    #         z=i
    # print(q[z])
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     q = [str(i) for i in range(a, b+1)]
#     m = []
#     for i in range(a, b+1):
#         digits = [int(j) for j in str(i)]
#         max_digit, min_digit = max(digits), min(digits)
#         m.append(max_digit - min_digit)
#     z = max(enumerate(m), key=lambda x: x[1])[0]
#     print(q[z])
# def max_min_difference(n):
#     digits = [int(d) for d in str(n)]
#     return max(digits) - min(digits)
# def find_max_diff_in_range(a, b):
#     max_diff_num = None
#     max_diff_value = 0
#     for i in range(a, b+1):
#         diff = max_min_difference(i)
#         if diff > max_diff_value:
#             max_diff_value = diff
#             max_diff_num = i
#     return max_diff_num
# for i in range((int(input()))):
#     a,b=map(int,input().split())
#     print(find_max_diff_in_range(a,b))
# def max_difference_in_range(a, b):
#     max_diff_value = 0
#     max_diff_number = 0
#     for n in range(a, b+1):
#         digits = [int(d) for d in str(n)]
#         max_digit, min_digit = max(digits), min(digits)
#         diff = max_digit - min_digit
#         if diff > max_diff_value:
#             max_diff_value = diff
#             max_diff_number = n
#     return max_diff_number
# def max_difference_in_range(a, b):
#     max_diff_value = float('-inf')
#     max_diff_number = -1
#     digit_dict = {}
#     for n in range(a, b+1):
#         if n not in digit_dict:
#             digits = [int(d) for d in str(n)]
#             digit_dict[n] = (max(digits), min(digits))
#         max_digit, min_digit = digit_dict[n]
#         diff = max_digit - min_digit
#         if diff > max_diff_value:
#             max_diff_value = diff
#             max_diff_number = n
#     return max_diff_number
# for i in range((int(input()))):
#     a,b=map(int,input().split())
#     print(max_difference_in_range(a,b))

import math
def solve():
    l, r = map(int, input().split())
    ans = 0
    dgt = l
    while l <= r and ans != 9:
        temp = [int(i) for i in str(l)]
        temp.sort()
        # print(temp)
        if temp[-1] - temp[0] > ans:
            ans = temp[-1] - temp[0]
            dgt = l
        l += 1
    print(dgt)
t = int(input())
for _ in range(t):
    solve()