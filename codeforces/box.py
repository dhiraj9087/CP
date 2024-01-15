# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range((int(input()))):
    n, a = int(input()), list(map(int, input().split()))
    l = 0
    flag = True
    j = 0
    for i in range(n):
        if a[i] != 0:
            l += 1
            a[i] = a[i] - 1
        elif a[i] == 0:
            flag = False
    # print(a)
    while flag and j < n:
        if a[j] != 0:
            l += 1
            a[j] = a[j] - 1
            j += 1
        elif a[j] == 0:
            flag = False
    
    print(l)

    # n = int(input())
    # s = list(map(int, input().split()))

    # # calculate the maximum number of tokens that can be put in each box
    # for i in range(1, n):
    #     s[i] = min(s[i], s[i-1])
    # # calculate the total number of tokens that can be put in all boxes
    # ans = 0
    # for i in range(n):
    #     ans += s[i]
    # print(ans)

    
