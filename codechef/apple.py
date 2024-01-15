def solve():
    m,n = list(map(int,input().split()))
    M = m
    if m==n:
        print("YES")
    elif m<n:
        print("NO")
    else:
        while M and M%2==0:
            M //= 2
        print("YES" if n%M==0 else "NO")
            

for _ in range((int(input()))):
    solve()
