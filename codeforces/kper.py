import math
import sys
input=sys.stdin.readline
def main():
    n, k = map(int, input().split())
    sign = ''
    ans = [n]
    for i in range(1, k):
        ans.append(ans[-1] - (n - i) // k - 1)
    ans.append(0)
    for i in range(1, k, 2):
        ans[i] = ans[i+1] + 1

    ans.pop()

    pos = 0
    while len(ans) < n:
        if sign == '+':
            ans.append(ans[pos] + 1)
            sign = ''
        else:
            ans.append(ans[pos] - 1)
            sign = ''
            pos += 1

    for i in range(len(ans)):
        print(ans[i], end=' ')

    print()
for _ in range(int(input())):
   main()