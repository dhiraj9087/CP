def main():
	n = int(input())
	a = list(map(int, input().split()))
	for i in range(n):
		for j in range(i + 2, n):
			if a[i] == a[j]:
				print("YES")
				return
	print("NO")
	
    
for _ in range(int(input())):
	main()
	