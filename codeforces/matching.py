for i in range((int(input()))):
    s=input()
    c=s.count('?')
    if c==0:
        print(0 if s[0]=='0' else 1)
    else:
        if c==len(s):
            print(9 if c==1 else 10**c-10**(c-1))
        else:
            if s[0]=='?':
                print(pow(10, c) - pow(10, c-1))
            else:
                print(0 if s[0]=='0' else 10**c)


