for i in range((int(input()))):
    n,k=map(int,input().split())
    s=input()
    # print(int(s,2))
    if s[0]!='1':
        k=k-1
        s = s[:0] + str(1) + s[1:]
    # print(k,s)
    for i in range(k):
        s=s+'0'
    print(s)