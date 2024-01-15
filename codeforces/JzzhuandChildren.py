import math

n, m = map(int, input().split())
v = list(map(int, input().split()))
ans = []
max_val = v[0] / m
ind = 0
for i in range(n):
    if math.ceil(v[i] / m) >= max_val:
        max_val = math.ceil(v[i] / m)
        ind = i + 1
print(ind)

