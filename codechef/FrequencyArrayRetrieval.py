# for i in range((int(input()))):
#     n,a=int(input()),(list(map(int,input().split())))
#     # print((a))
#     d={}
#     flag=True
#     for i in a:
#         if i in d:
#             d[i] += 1
#         else:
#             d[i] = 1
#     # print(d)
#     # d2={}
#     # for i in range(1,len(d)+1):
#     #     d2[i]=a.count(a[i-1])
#     # print(d2)
#     # for i in d:
#     #     if d[i]<i:
#     #         print("-1")
#     #         break
    
#     for i in d:
#         if d[i]%i!=0:
#             print("-1")
#             flag=False
#             break
#     if flag:
#         d2={}
#         num=1
#         for i in a:
#             if i not in d2:
#                 d2[i]=num,i-1
#                 num+=1
#             else:
#                 if d2[i][1]!=0:
#                     num2,i2=d2[i]
#                     d2[i]=num2,i2-1
#                 else:
#                     d2[i]=num,i-1
#                     num+=1
                    
#             print(d2[i][0],end=' ')
        
#         print()
    
    


# from collections import Counter

# for _ in range(int(input())):
#     d2={}
#     n = int(input())
#     a = list(map(int, input().split()))
#     d = Counter(a)
#     print(d)
#     flag = True
#     print("-1") if any(d[i] % i != 0 for i in d) else print(*(d2[i][0] if i in d2 else d2.setdefault(i, (num, i - 1))[0] for num, i in enumerate(a, start=1)), end=' ')
#     print()from collections import defaultdict

