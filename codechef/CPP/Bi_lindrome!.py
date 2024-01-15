# cook your dish here
for i in range((int(input()))):
    n=int(input())
    s=input()
    q=[]
    c=0
    for i in range(len(s)):
        a=s[i]
        q.append(s.count(a))
    #print(q)
    #print(abs(max(set(q))-n))
    # if(len(set(q))==1):
    #     print("-1")
    # else:
    #     print(abs(max(set(q))-n))


    for i in range(n):
        d=s[i]
        if(s.count(d)==min(q)):
            c+=1
    if(c==n):
        print("-1")
    else:
        print(c)