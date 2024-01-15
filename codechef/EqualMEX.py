# # from collections import defaultdict
# def solve():
#     n = int(input())
#     # mp = defaultdict(int)
#     mp={}
#     a=list(map(int,input().split()))
#     # s=len(set(a)
#     for i in range(2*n):
#         if i not in a:
#             mp[i]=0
#         else:
#             mp[i]
#     print(mp)
#     # for i in range(2*n):
#     #     if mp[i] == 0:
#     #         print("YES")
#     #         return
#     #     if mp[i] == 1:
#     #         print("NO")
#     #         return
#     # print("YES")  

    
# for _ in range((int(input()))):
#     solve()
from collections import defaultdict

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    count_dict = defaultdict(int)

    for num in a:
        count_dict[num] += 1
    # print(count_dict)
    for i in range(2 * n):
        if count_dict[i] == 0:
            print("YES")
            return
        if count_dict[i] == 1:
            print("NO")
            return
    print("YES")

for _ in range(int(input())):
    solve()
