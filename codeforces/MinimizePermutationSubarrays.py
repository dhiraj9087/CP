def main():
    n=int(input())
    a=list(map(int,input().split()))
    # for i in range(n-2):
    #     if a[i]==1:
    #         c=i+1
    #         if a[i+1]!=2 and a[i-1]!=2:
    #             print(1,1)
    #             return
    #         if a[i+1]==2:
    #             if a[i+2]==3:
    #                 print(i+2,1)
    #                 return
    #             else:
    #                 print(i+2,n)
    #                 return
    #         if a[i-1]==2:
    #             if a[i-2]==3:
    #                 print(i,1)
    #                 return
    #             else:
    #                 print(i,n)
    #                 return
    o=a.index(1)+1
    t=a.index(2)+1
    m=a.index(max(a))+1
    if m>t and m>o:
        if o>t:
            print(m,o)
            return
        else:
            print(m,t)
            return
    if m<t and m<o:
        if o>t:
            print(m,t)
            return
        else:
            print(m,o)
            return
    print(n,n)
            
for _ in range((int(input()))):
    main()