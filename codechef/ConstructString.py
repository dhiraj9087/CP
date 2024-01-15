# for i in range((int(input()))):
#     n=int(input())
#     a=input()
#     s=""
#     d={}
#     q=[]
#     for i in a:
#         d[i]=a.count(i)
#     for i in range(len(a)-2):
#         if a[i]==a[i+1]==a[i+2]:
#             q.append(a[i])
#     print(q)
    # for i in a:
    #     d[i]=a.count(i)
    # # print(d)
    # for i in d:
    #     if d[i]%2!=0:
    #         s=s+i
    #     else:
    #         s=s+i+i
    # print(s)
    
    # for i in a:
    #     if i not in s:
    #         s=s+i
    # print(s)
# cook your dish here
# t = int(input())
# for i in range(t):
#     n = int(input())
#     s = input()
#     a = 0
#     b,c=[],[]
#     for i in s:
#         if i not in c:
#             c.append(i)
#     # c = list(set(s))
#     # print(c)
#     for i in range(len(c)):
#         if(s.count(c[i])%2!=0 ):
#             a+=1
#             b.append(c[i])
#         else:
#             for k in range(2):
#                 b.append(c[i])
#     sorted(b)
#     for i in b:
#         print(i,end="")
#     print()
# for (int i = 0; i < n; i++)
#     {
#         cmp++;
#         if (s[i] != s[i + 1])
#         {
#             v.push_back(cmp);
#             cmp = 0;
#         }
#     }
# import sys
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     s = input().strip()
#     # print(s)
#     v = []
#     cmp = 0
#     for i in range(n-1):
#         cmp += 1
#         if s[i] != s[i + 1]:
#             v.append(cmp)
#             cmp = 0
#     ans = ""
#     ind = 0
#     print(v)
#     for i in range(len(v)):
#         if v[i] % 2:
#             ans += s[ind]
#             ind += v[i]
#         else:
#             ans += s[ind]*2
#             ind += v[i]
#     print(ans)

# t = int(input())
# for _ in range(t):
#     solve()
# Python code equivalent of the given C++ code

# MOD = 1000000007

# def solve():
#     n = int(input())
#     s = input().strip()
#     v = []
#     cmp = 0
#     for i in range(n):
#         cmp += 1
#         if i < n - 1 and s[i] != s[i + 1]:
#             v.append(cmp)
#             cmp = 0
#     ans = ""
#     ind = 0
#     for i in range(len(v)):
#         if v[i] % 2 == 1:
#             ans += s[ind]
#             ind += v[i]
#         else:
#             ans += s[ind] * 2
#             ind += v[i]
#     print(ans)

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         solve()
# MOD = 1000000007

# def solve():
#     n = int(input())
#     s = input().strip()
#     v = []
#     cmp = 0
#     for i in range(n):
#         cmp += 1
#         if i < n - 1 and s[i] != s[i + 1]:
#             v.append(cmp)
#             cmp = 0
#     ans = ""
#     ind = 0
#     for i in range(len(v)):
#         if v[i] % 2 == 1:
#             ans += s[ind]
#             ind += v[i]
#         else:
#             ans += s[ind]
#             ans += s[ind + 1]
#             ind += v[i]
#     print(ans)
# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         solve()



# for i in range((int(input()))):
#     n = int(input())
#     s = input().strip()
#     var = s[0]
#     c = ""
#     a = 1
#     for i in range(1, n):
#         if var == s[i]:
#             a += 1
#         else:
#             if a % 2 == 0:
#                 c += var * 2
#             else:
#                 c += var
#             var = s[i]
#             a = 1
#     if a % 2 == 0:
#         c += var * 2
#     else:
#         c += var
#     print(c)
for i in range((int(input()))):
    n = int(input())
    string_input = input().strip()
    var = string_input[0]
    count = ""
    q = 1
    for i in range(1, n):
        if var == string_input[i]:
            q += 1
        else:
            if q % 2 == 0:
                count += var * 2
            else:
                count += var
            var = string_input[i]
            q = 1
    if q % 2 == 0:
        count += var * 2
    else:
        count += var
    print(count)

