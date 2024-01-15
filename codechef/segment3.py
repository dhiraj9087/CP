def main():
    n = int(input())
    a = list(map(int, input().split()))
    c = float('inf')
    for x in range(3):
        for y in range(3):
            times = 0
            a1 = a[0]
            a2 = a[1]
            while a1 % 3 != x:
                times += 1
                a1 += 1
            while a2 % 3 != y:
                times += 1
                a2 += 1
            for k in range(2, n):
                a3 = a[k]
                sum = a1 + a2 + a3
                if sum % 3:
                    times += (3 - (sum % 3))
                    a3 += (3 - (sum % 3))
                a1 = a2
                a2 = a3
            c = min(c, times)
    print(c)

for _ in range(int(input())):
    main()