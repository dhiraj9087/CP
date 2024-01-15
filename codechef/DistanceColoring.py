mod = 1000000007
def main():
    n, m = map(int, input().split())
    a = 1
    while n and m:
        a = (a * m) % mod
        n -= 1
        m-=1
    print(a)
for _ in range((int(input()))):
    main()