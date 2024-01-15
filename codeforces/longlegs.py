
import math

def solve():
    x, y = map(int, input().split())
    a = min(x, y)
    b = max(x, y)
    ans = math.inf
    for i in range(1, 100001):
        curr = (a + i-1)//i + (b + i-1)//i + i-1
        ans = min(ans, curr)
        # print(ans)

    print(ans)

tc = int(input())
for _ in range(tc):
    solve()