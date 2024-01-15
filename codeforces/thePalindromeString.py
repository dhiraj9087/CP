for i in range((int(input()))):
    s=input()
    a=set(s)
    print('-1' if len(set(s))==1 else len(s)-1)
    # print(len(s))
    # d={}
    # for i in s:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    # # print(d)
    # if len(d)==1:
    #     print(-1)
    # else:
    #     flag=True
    #     i=1
    #     c=0
    #     while flag:
    #         # a=len(s)//2
    #         s=s[i::]
    #         if len(s)<=1 or s!=s[::-1]:
    #             c+=1
    #             flag=False
    #         else:
    #             i+=1
    #     if c>0:
    #         print(len(s))
    #     else:
    #         print('-1')
    # s=s[1::]
    # print(s)
    # print(a)
    # if len(a)==1:
    #     print(-1)
    # else:
    #     print(len(s)-1)
        

    
        
        