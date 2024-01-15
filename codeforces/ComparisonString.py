def main():
    n=int(input())
    s=input()
    # j=1
    # for i in range(n):
    #     if s[i]=='<':
    #         j+=1
    # pre_a = [0] * (n + 1)
    # for i in range(n):
    #     if s[i] == '<':
    #         pre_a[i + 1] = pre_a[i] + 1
    #     else:
    #         pre_a[i + 1] = pre_a[i] - 1
    # print(pre_a)
    # print(len(set(pre_a)))
    m = 0
    c1 = 0
    c2 = 0
    for i in s:
        if i == '<':
            c1 += 1
        else:
            m = max(m, c1)
            c1 = 0
    m = max(m, c1)
    for i in s:
        if i == '>':
            c2 += 1
        else:
            m = max(m, c2)
            c2 = 0
    m = max(m, c2)
    print(m + 1)

for _ in range((int(input()))):
    main()
