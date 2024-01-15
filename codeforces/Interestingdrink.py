n=int(input())
a=list(map(int,input().split()))
a.sort()
q=int(input())
# z=[]
min_a=a[0]
max_a=a[n-1]
for i in range(q):
    s=int(input())
    # z.append(s)
    if s>=max_a:
        print(n)
    elif s<min_a:
        print(0)
    else:
        l, r = 0, n-1
        while l < r:
            mid = (l + r) // 2
            if a[mid] <= s:
                l = mid + 1
            else:
                r = mid
        print(l)

        
# print(z,a)

