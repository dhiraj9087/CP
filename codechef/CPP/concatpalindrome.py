for i in range((int(input()))):
    a,b=map(int,input().split())
    s1=input()
    s2=input()
    s=s1+s2
    #print(s)
    d1={}
    d2={}
    c=0
    for i in s1:
        d1[i]=s1.count(i)
    #print(d1)
    for i in s2:
        d2[i]=s2.count(i)
    #print(d2)
    d2.update(d1)
    #print(d2)
    for i in d2.values():
        if(i%2==0):
            c+=1
    #print(c)
    if(c>1):
        print("NO")
    else:
        print("YES")
    #print(d.values())
    # for i in d.values():
    #     #if(i%2!=0):
    #     c+=i%2
    # print(c)
    # # if(c>1):
    # #     print("NO")
    # # else:
    # #     print("YES")