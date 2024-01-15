def solve():
    n, k = map(int, input().split())
    for i in range(n - k, n + 1):
        print(i, end=" ")
    for i in range(n - k - 1, 0, -1):
        print(i, end=" ")
    print()

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
