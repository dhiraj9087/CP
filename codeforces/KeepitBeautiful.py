# for _ in range(int(input())):
#     n=int(input())
#     a=list(map(int,input().split()))
#     l, r = a[0], 0
#     ans = [l]
#     while r < n:
#         r += 1
#         if a[r] < l or a[r] >= ans[r - 1]:
#             ans.append(a[r])
#         else:
#             break
#     print(ans)
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = "1"
        p, q = True, True
        x = int(input())
        y = 0
        mx = x
        mn = x
        y = x
        v = [0] * n
        for i in range(1, n):
            x = int(input())
            if x >= y and p:
                s += '1'
                y = x
            elif x > mx:
                s += '0'
            else:
                p = False
                if q:
                    mn = x
                    q = False
                if x >= mn:
                    s += '1'
                    mn = x
                else:
                    s += '0'
        print(s)
     
if __name__ == "__main__":
    main()