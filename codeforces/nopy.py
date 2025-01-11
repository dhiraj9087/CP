def solve():
    n, k = map(int, input().split())
    # Create frequency array directly without creating list first
    freq = {}
    for x in map(int, input().split()):
        freq[x] = freq.get(x, 0) + 1
    
    # Get only values and sort them
    freqs = sorted(freq.values())
    
    remaining = k
    total = len(freqs)
    # Start from smallest frequencies
    for f in freqs:
        if f <= remaining:
            remaining -= f
            total -= 1
        else:
            break
            
    print(max(1, total))

# Fast input processing
t = int(input())
for _ in range(t):
    solve()