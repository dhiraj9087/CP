# def factor(n,a):
#     n1=n//3
#     n2=n-(n//3)
#     a.append(n1)
#     a.append(n2)

# def solve(n,m):
#     if n<m:
#         return 'NO'
#     a=[]
#     factor(n,a)
#     # flag=True
#     c=0
#     while c==0:
#         if m not in a:
#             factor(a[len(a)-1],a)
#         else:
#             # flag=False
#             c=1
#             return 'YES'
        
#     # a.append(n//3)
#     # a.append(n-n//3)
#     # return a 

# for i in range((int(input()))):
#     n,m=map(int,input().split())
#     print(solve(n,m))

def factor(n, m):
    if n == m:
        return True
    elif n % 3 != 0:
        return False
    else:
        return factor(n // 3, m) or factor(2 * n // 3, m)

def solve():
    n, m = map(int, input().split())
    print("YES" if factor(n, m) else "NO")

for _ in range((int(input()))):
    solve()
