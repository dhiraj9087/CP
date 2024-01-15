for i in range((int(input()))):
    n=int(input())
    s=input()
    a,b=0,0
    for i in range(len(s)):
        if s[i]=='1':
            if (i)%2==0:
                a+=1
            else:
                b+=1
    # print(a,b)
    if a>0 and b>0:
        print("1")
    else:print("2")
    
    # print(c)
    # for i in range(n):
    # a=s.index('1')
    # print(a)
    