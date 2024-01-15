# def main():
#     n,b=map(int,input().split())
#     a=list(map(int,input().split()))
#     a=set(a)
#     a=list(a)
#     for i in range(n):
#         for j in range(i+1,n):
#             if a[i] & a[j] == b:
#                 print("YES")
#                 return
#     print("NO")
# for _ in range(int(input())):
#     main()

def solve():
    n, b = map(int, input().split())
    a = list(map(int, input().split()))
    o = []
    z = []
    i = 0
    temp = b
    while temp > 0:
        if temp & 1:
            o.append(i)
        else:
            z.append(i)
        i += 1
        temp = temp >> 1
    c = []
    for i in a:
        temp1 = b
        temp2 = i
        isone = True
        while temp1 > 0:
            last1 = (temp1 & 1)
            last2 = (temp2 & 1)
            if last1 == 1 and last2 == 0:
                isone = False
            temp1 = temp1 >> 1
            temp2 = temp2 >> 1
        if isone:
            c.append(i)
    if not c:
        print("NO")
        return
    ans = c[0]
    for i in c:
        ans = (ans & i)
    if ans == b:
        print("YES")
        return
    print("NO")


for _ in range(int(input())):
    solve()
