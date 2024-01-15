for i in range((int(input()))):
    n=int(input())
    s=input()
    a="1"
    for i in range(n-1):
        a=a+str(int(s[i])^int(a[i]))
    print(a.count('1'))
