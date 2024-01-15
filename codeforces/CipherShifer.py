# def main():
#     n=int(input())
#     a=input()
#     # if a[0]==a[n-1]:
#     #     print(a[0])
#     #     return
#     first=a[0]
#     s=""
#     s=s+first
#     for i in range(1,n):
#         if a[i]==first:
#             s=s+a[i]
#             first=a[i+1]
            
#     print(s)  
#     # n = int(input())
#     # s = input().strip()
#     # ans = ""
#     # cmp = s[0]
#     # for i in range(1, n):
#     #     if s[i] == cmp:
#     #         ans += s[i]
#     #         cmp = s[i + 1]
#     #         i += 1
#     # print(ans)  
    
# for _ in range((int(input()))):
#     main()
# # n = int(input())
# #     s = input().strip()
# #     ans = ""
# #     cmp = s[0]
# #     for i in range(1, n):
# #         if s[i] == cmp:
# #             ans += s[i]
# #             cmp = s[i + 1]
# #             i += 1
# #     print(ans)
def solve():
    n = int(input())
    s = input()
    result = ""
    first= s[0]
    i = 1
    while i < n:
        if s[i] == first:
            result += s[i]
            if i < n-1:
                first = s[i + 1]
            i += 2
        else:
            i += 1
    print(result)


for _ in range(int(input())):
    solve()
