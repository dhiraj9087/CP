# def solve():
#     n,k=map(int,input().split())
#     a=list(map(int,input().split()))
#     a.sort()
#     # print(a)
#     s2_for=[0]*n
    
#     for i in range(0,n-1,2):
#         s2_for[i+1]=a[i]+a[i+1]
#     print(s2_for,a)

# for _ in range((int(input()))):
#     solve()
for _ in range(int(input())):
	n, k = map(int, input().split())
	a = sorted(list(map(int, input().split())))
	ans = 0
	pr = [0] * (n + 1)
	for i in range(n):
		pr[i + 1] = pr[i] + a[i]
	# print(pr)
	for i in range(k + 1):
		ans = max(ans, pr[n - (k - i)] - pr[2 * i])
	print(ans)
	