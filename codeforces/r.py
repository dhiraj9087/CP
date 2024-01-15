for i in range((int(input()))):
    s=input()
    a='codeforces'
    c=0
    for i in range(len(s)):
        if s[i]!=a[i]:
            c+=1
    print(c)