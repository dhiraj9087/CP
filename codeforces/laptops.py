

def solve():
    n = int(input())
    
    while n:
        a, b = map(int, input().split())
        
        if a != b:
            print("Happy Alex")
            return
        n -= 1
    print("Poor Alex")

if __name__ == "__main__":
    solve()
