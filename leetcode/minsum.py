n = 13
target = 50
if n==1:
    print(1)
elif target//2 > n:
    print(n*(n+1)//2)
else:
    # # a=[1,target]
    # # add=(1+target)
    # # while len(a)!=n:
    # #     target+=1
    # #     a.append(target)
    # #     add+=target
    # # print(a)
    # a=[]
    # ans=0
    # while len(a)!=target//2:
    #     ans+=1
    #     a.append(ans)
    # i=target-1
    # while len(a)!=n:
    #     i+=1
    #     ans+=i
    #     a.append(i)
        
    

    # print(sum(a))
    a=target//2
    # print(a)
    ans=a*(a+1)//2
    # print(ans)
    rem=target-a-1
    # print(rem)
    add=n+rem
    final=(add*(add+1)//2) - ((target-1)*target//2) + ans
    print(final)

