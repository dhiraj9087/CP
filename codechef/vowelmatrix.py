def main():
    mod = 1000000007
    n, k = map(int, input().split())
    s = input().strip()
    m = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True
    }
    ans, ct1, ct2 = 1, 0, 0
    first, flag = False, False
    for i in s:
        if m.get(i):
            if not first:
                if flag:
                    ct2 += 1
                    ans = (ans * ct2) % mod
            ct1 += 1
            first = True
            flag = True
            ct2 = 0
        else:
            if not first:
                ct2 += 1
        if ct1 == k:
            first = False
            ct1 = 0
    ans = ans % mod
    print(ans)


for _ in range(int(input())):
    main()
