def solve():
        z, a = map(int, input().split())
        if z // a > 1:
            if a == 1:
                s = sum(range(1, z+1))
                if s % 2 == 0:
                    print("no")
                else:
                    print("yes")
            else:
                if z % 2 == 0:
                    c = a - 1
                    d = z // 2 - c
                    if d % 2 == 0:
                        print("no")
                    else:
                        print("yes")
                else:
                    c = a - 1
                    d = (z // 2) + 1 - c
                    if d % 2 == 0:
                        print("no")
                    else:
                        print("yes")
        else:
            print("no")
for _ in range((int(input()))):
    solve()
