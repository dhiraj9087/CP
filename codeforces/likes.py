import sys
input = sys.stdin.readline
for i in range((int(input()))):
    N = int(input())
    a=list(map(int,input().split()))
    x, y, z = 0, 0, 0
    for i in range(len(a)):
        # x = int(input())
        if a[i] > 0:
            y += 1
        else:
            z += 1
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i] = i + 1 if i < y else 2 * y - i - 1
    for i in range(N):
        B[i] = i % 2 ^ 1 if i < 2 * z else i - 2 * z + 1
    print(*A)
    print(*B)