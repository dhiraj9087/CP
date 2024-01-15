
import sys

for line in sys.stdin:
    t = int(line)
    for _ in range(t):
        n = int(input())
        if n % 2 == 0:
            z, x = 1, 1
            for i in range(1, n // 2 + 1):
                for j in range(1, n + 1):
                    print(2 * z - 1, end=" ")
                    z += 1
                print()
            for i in range(1, n // 2 + 1):
                for j in range(1, n + 1):
                    print(2 * x, end=" ")
                    x += 1
                print()
        else:
            z, x, a = 1, 1, n
            for i in range(1, n // 2 + 1):
                for j in range(1, n + 1):
                    print(2 * z - 1, end=" ")
                    z += 1
                print()
            for i in range(0, (n // 2) + 1):
                print(n * n - a + 1, end=" ")
                a = a - 2
            for i in range((n // 2) + 1, n):
                print(2 * x, end=" ")
                x += 1
            print()
            for i in range(1, n // 2 + 1):
                for j in range(1, n + 1):
                    print(2 * x, end=" ")
                    x += 1
                print()
