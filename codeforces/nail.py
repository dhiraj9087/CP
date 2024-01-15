import sys
def main():
    n=int(input())
    count=0
    for i in range(n):
        a, b = map(int, sys.stdin.readline().split())
        if a>b:count+=1
    print(count)
for _ in range(int(input())):
    main()
