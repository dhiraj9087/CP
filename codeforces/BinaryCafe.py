import math

def solve():
    n, k = map(int, input().split())
    num = 50
    k = min(num, k)
    cmp = int(math.log2(n))
    ans = n + 1
    if cmp < k:
        print(ans)
        return
    print(int(math.pow(2, k)))

for i in range(int(input())):
    solve()
