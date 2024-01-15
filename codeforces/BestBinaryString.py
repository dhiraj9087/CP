def main():
    # s=input()
    # if '?' not in s:
    #     print(s)
    #     return
    # a=list(s)
    # flag=False
    # for i in range(len(s)):
    #     if s[i]=='1':flag=True
    #     if s[i]=='?' and flag==False:
    #         a[i]='0'
    #     elif s[i]=='?' and flag==True:
    #         a[i]='1'        
    # # print(*a)
    # for i in a:
    #     print(i,end='')
    # print()
    s = input().strip()
    n = len(s)
    a=list(s)
    for i in range(n):
        if a[i] == '?':
            a[i] = '0'
        else:
            break
    for i in range(n-1, -1, -1):
        if a[i] == '?':
            a[i] = '1'
        else:
            break
    # print(s)
    for i in range(1, n):
        if a[i] == '?':
            a[i] = a[i-1]
    # print(a)
    for i in a:
        print(i,end='')
    print()
for _ in range((int(input()))):
    main()

    