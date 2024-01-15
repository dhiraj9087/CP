# def solve():
#     n=int(input())
#     a=list(map(int,input().split()))
#     diff = a[1] - a[0]
#     for i in range(2, n):
#         if a[i] - a[i-1] != diff:
#             return False
#     return True
def solve():
    n=int(input())
    a=list(map(int,input().split()))
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (a[j] - a[i] == a[k] - a[j]):
                    return False
    return True

for _ in range((int(input()))):
    if solve():
        print("Yes")
    else:
        print("No")
    # print(solve())
    