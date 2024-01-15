for i in range((int(input()))):
    a=int(input())
    s=input()
    c=0
    q1,q2=[],[]
    # for i in range(len(s)-2):
    #     if s[i]==s[i+2]:
    #         c+=1
    #print(c)
    # if len(s)==len(set(s)):
    #     print("YES")
    # elif c>1:
    #     print("YES")
    # else:
    #     print("NO")
    for i in range(0,len(s),2):
        q1.append(s[i])
    for i in range(1,len(s),2):
        q2.append(s[i])
    #print(q1,q2)
    for i in q1:
        if i in q1 and i in q2:
            c+=1
    #print(c)
    if c>0:
        print("NO")
    else:
        print("YES")

    # for i in s:
    #     print(s.count(i),end=' ')
    # print()