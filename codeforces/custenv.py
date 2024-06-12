def modpower(base, exp, mod=10**9+7):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def main():
    l, r, k = map(int, input().split())
    if k >= 10:
        print(0)
        return
    
    av = 10 // k
    if 10 % k != 0:
        av += 1
    
    mod = 10**9 + 7
    rt = modpower(av, r, mod)
    lt = modpower(av, l, mod)
    ans = (rt - lt + mod) % mod
    
    print(ans)

# Example usage
if __name__ == "__main__":
    for _ in range(int(input())):
        main()
