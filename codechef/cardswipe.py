def main():
    # n=int(input())
    # a=list(map(int,input().split()))
    # q=[]
    # # c=float('-inf')
    # c=0
    # ans=0
    # len=0
    # for i in range(n):
    #     if a[i] not in q:
    #         # c+=1
    #         # c=max()
    #         q.append(a[i])
    #         len+=1
    #     else:
    #         if a[i] in q:
    #             q.remove(a[i])
    #             len-=1
    #         else:
    #             q.append(a[i])
    #             len+=1
    #         c+=1
    #         ans=max(ans,c)
    # ans=max(len,ans)
    # print(ans)
    n = int(input())
    a = list(map(int, input().split()))

    
    # if len(set(a)) == 1 or len(set(a)) == n:
    #     print(len(set(a)))
    # else:
    #     c = []
    #     flag = 0
    #     ans = 0
        
    #     for i in a:
    #         if i not in c:
    #             c.append(i)
    #             flag += 1
    #             ans = max(flag, ans)
    #         else:
    #             flag -= 1
    #             c.remove(i)
        
    #     print(ans)
    dict = {}
    ans = 0
    c = 0
    
    for num in a:
        
        if num not in dict:
            c += 1
            dict[num] = True
            ans = max(ans, c)
        else:
            c-=1
            del dict[num]
    
    ans = max(ans, len(dict))
    print(ans)



for _ in range(int(input())):
    main()