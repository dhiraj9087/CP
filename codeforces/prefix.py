for _ in range((int(input()))):
    n = int(input())
    s1 = []
    a=list(map(str,input().split()))
    a.sort(key=len)
    # print(a)
    flag=True
    for i in range(0, 2*n-2, 2):
        a[i] = a[i][::-1]
        # print()
        if a[i] != a[i+1]:
            flag=False
    if flag:
        print("YES")
    else:
        print("NO")
    