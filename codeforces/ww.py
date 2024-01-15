from collections import Counter
s = "cbaebabacd"
p = "abc"
if len(s) < len(p):
    print([])
need = Counter(p)
print(need)
cur, lo = 0, 0
ret = []
for i, c in enumerate(s):
    print(i,c)
    need[c] -= 1
    cur += 1
    while need[c] < 0:
        need[s[lo]] += 1
        lo += 1
        cur -= 1
    if cur == len(p):
        ret.append(lo)
# print(ret)