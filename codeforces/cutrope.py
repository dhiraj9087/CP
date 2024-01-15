import sys
 
input = sys.stdin.readline

def main():
    n=int(input())
    c=0
    for i in range(n):
        a,b=map(int,input().split())
        if a>b:
            c+=1
    print(c)


for _ in range(int(input())):
    main()