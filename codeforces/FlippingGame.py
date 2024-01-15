def main():
    a, b, c = map(int,input().split())
    print(1 if a < c else -1, b if c < b * a else -1)
for i in range((int(input()))):
    main()