import math
import sys
input=sys.stdin.readline
def num(x,y):
    a = (x + y) // 2
    b = (x - y) // 2
    return a, abs(b)
def main():
    n = int(input())
    a = list(map(int, input().split()))
    even,odd=[],[]
    for i in a:
        if i % 2==1:
            odd.append(i)
        else:
            even.append(i)
    if len(odd) % 2 or len(even) % 2:
        print(-1)
        return
    odd.sort()
    even.sort()
    s1, s2 = len(odd) // 2, len(even) // 2
    v1, v2 = [], []
    for i in range(s1):
        v1.extend([(odd[i + s1] + odd[i]) // 2, (odd[i + s1] - odd[i]) // 2])
    for i in range(s2):
        v2.extend([(even[i + s2] + even[i]) // 2, (even[i + s2] - even[i]) // 2])
    ans = []
    for i in range(0, 2 * s1, 2):
        ans.append(v1[i])
    for i in range(0, 2 * s2, 2):
        ans.append(v2[i])
    for i in range(1, 2 * s1, 2):
        ans.append(v1[i])
    for i in range(1, 2 * s2, 2):
        ans.append(v2[i])
    print(*ans)

for _ in range(int(input())):
   main()