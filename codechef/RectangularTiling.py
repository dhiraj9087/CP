def main():
    n, m = map(int, input().split())

    if ((2 * n) % 4 == 0) or ((2 * m) % 4 == 0):
        print("YES")
        return
    else:
        print("NO")
        return
for _ in range((int(input()))):
    main()