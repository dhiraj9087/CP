for i in range((int(input()))):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[n - 1]
    for i in range(n - 2, -1, -1):
        if a[i] != ans:
            ans += a[i]
            break
    print(ans)
