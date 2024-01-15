n, k = map(int, input().split())
if n % 2 == 0:
    mid = n // 2
    if k <= mid:
        print(2*k - 1)
    else:
        print(2*(k - mid))
else:
    mid = (n + 1) // 2
    if k <= mid:
        print(2*k - 1)
    else:
        print(2*(k - mid))
