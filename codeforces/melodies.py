def solve():
    n=int(input())
    s=input()
    a = set()
    for i in range(n - 1):
        a.add(s[i]+s[i+1])
    print(len(a))
for _ in range((int(input()))):
    solve()
