for i in range((int(input()))):
    n=int(input())
    s=input()
    # t=""
    alice,bob=[],[]
    if n%2==0:
        for i in range(len(s)//2):
            alice.append(s[i])
        # print(alice)
        for i in range(len(s)-1,len(s)//2-1,-1):
            bob.append(s[i])
        # print(*alice,*bob)
        t=""
        for i in range(len(alice)):
            if alice[i] == '0':
                t = alice[i] + t
            if bob[i] == '1':
                t = bob[i] + t
            if alice[i] == '1':
                t = t + alice[i]
            if bob[i] == '0':
                t = t + bob[i]
        print(t)
    else:
        for i in range(len(s)//2+1):
            alice.append(s[i])
        # print(alice)
        for i in range(len(s)-1,len(s)//2,-1):
            bob.append(s[i])
        # print(alice,bob)
        t=""
        for i in range(len(bob)):
            if alice[i] == '0':
                t = alice[i] + t
            if bob[i] == '1':
                t = bob[i] + t
            if alice[i] == '1':
                t = t + alice[i]
            if bob[i] == '0':
                t = t + bob[i]
        if alice[len(alice)-1] == '0': t = alice[len(alice)-1] + t
        else: t = t + alice[len(alice)-1]
        print(t)

