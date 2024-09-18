def count_max_arrangements(N, P):
    MOD = 998244353
    
    fixed = sum(1 for i in range(0, 2*N, 2) if P[i] != 0)
    
    return pow(N - fixed, N, MOD)

T = int(input())
for _ in range(T):
    N = int(input())
    P = list(map(int, input().split()))
    print(count_max_arrangements(N, P))