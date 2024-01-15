# def solve():
#     m,s=map(int,input().split())
#     a=list(map(int,input().split()))
#     # 1 2 3 4 5 6
#     add,i=0,0
#     if m>s:
#         return 'NO'
#     while add<s:
#         if i not in a:
#             add+=i
#             a.append(i)
#         if add ==s :
#             return 'YES'
#         i+=1
#     return 'NO'


def solve():
    n, s = map(int, input().split())
    a = [int(x) for x in input().split()]
    s += sum(a)
    sm = 0
    cnt = 0
    for i in range(1, s + 1):
        if sm >= s:
            break
        sm += i
        cnt = i
    if sm != s or max(a) > cnt or cnt <= n:
        return 'NO'
    else:
        return 'YES'Divisible Array

for _ in range((int(input()))):
    print(solve())