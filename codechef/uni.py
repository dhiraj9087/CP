import math
import sys
input=sys.stdin.readline
def main():
    n, k = map(int, input().split())
    s = input()
    v1 = [0] * k
    v2 = [0] * k

    for i in range(n):
        ind = i % k
        if s[i] == '0':
            v2[ind] += 1
        else:
            v1[ind] += 1

    a, b = 0, 0

    for i in range(k):
        if v1[i] % 2 == 1:
            a += 1 + ((v1[i] + 1) // 2)
        else:
            a += v1[i] // 2

    for i in range(k):
        if v1[i] == 0:
            b = float('inf')
            break
        else:
            b += v2[i]

    print(min(a, b))

for _ in range(int(input())):
   main()