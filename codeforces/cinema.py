n = int(input())
ticket = list(map(int, input().split()))
if ticket[0] != 25:
    print("NO")
else:
    p25, p50, p100 = 0, 0, 0
    flag = True
    for x in ticket:
        if x == 25:
            p25 += 1
        elif x == 50:
            if p25 >= 1:
                p25 -= 1
                p50 += 1
 
            else:
                flag = False
                break
 
        else:
            if p50 >= 1 and p25 >= 1:
                p50 -= 1
                p25 -= 1
                p100 += 1
            elif p25 >= 3:
                p25 -= 3
                p100 += 1
 
            else:
                flag = False
                break
 
    if flag:
        print("YES")
    else:
        print("NO")
    