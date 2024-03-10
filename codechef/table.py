# import math
# import sys
# input=sys.stdin.readline
# def main():
#     n=int(input())
#     a=list(map(int,input().split()))
#     a.sort(reverse=True)
#     ans = 0
#     for i in range(n):
#         temp = a[i] * (i + 1)
#         ans = max(ans, temp)
#     print(ans)
# for _ in range(int(input())):
#    main()
t=int(input())
for test in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    values.sort(reverse=True)
    max_product = 0
    for i in range(n):
        temp = values[i] * (i + 1)
        max_product = max(max_product, temp)
    print(max_product)


