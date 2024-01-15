import sys
input = sys.stdin.readline

for i in range((int(input()))):
    n, k = map(int, input().split())
    q = []
    for i in range(n):
        s=input()
        q.append(s)
    c = q[0]
    # print(cmp,v)
    res = 1
    for i in range(1, n):
        if q[i] == c:
            res += 1
    print(res)



