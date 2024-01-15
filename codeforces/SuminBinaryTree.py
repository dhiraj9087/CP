def main():
    n=int(input())
    add=0
    while n:
        add+=n
        n=n//2
    print(add)
for _ in range(int(input())):
    main()