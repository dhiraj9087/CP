import math
import sys
input=sys.stdin.readline
from collections import deque
def main():
    n, m = map(int, input().split())
    a = deque(map(int, input().split()))
    b = deque(map(int, input().split()))
    a = deque(sorted(a))
    b = deque(sorted(b, reverse=True))
    ans = []
    while len(ans) < n:
        if abs(b[-1] - a[-1]) > abs(b[0] - a[0]):
            ans.append(abs(b.pop() - a.pop()))
        else:
            ans.append(abs(a.popleft() - b.popleft()))
    total = sum(ans)
    print(total)
for _ in range(int(input())):
   main()