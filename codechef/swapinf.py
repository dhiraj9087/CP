def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = input()
        b = input()
        
        if a == b and (a == "01" or a == "10") and k % 2 == 1:
            print("NO")
            continue
        
        add = 0
        temp = 0
        F = 0
        for i in range(n):
            if a[i] != b[i]:
                add += 1
                temp += int(a[i])
            else:
                F += 1
        
        if add == 2 and len(a) == 2 and k % 2 == 0:
            print("NO")
            continue
        
        if add == temp * 2 and temp <= k:
            print("YES")
        else:
            print("NO")

main()
















