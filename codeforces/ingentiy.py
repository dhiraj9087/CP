# import math
# import sys
# input=sys.stdin.readline
# def main():
#     n=int(input())
#     s=input().strip()
#     x,y=0,0
#     for i in range(n):
#         if s[i]=='N':
#             y+=1
#         elif s[i]=='S':
#             y-=1
#         elif s[i]=='E':
#             x+=1
#         else:
#             x-=1
#     if abs(x)%2==1 or abs(y)%2==1:
#         print("NO")
#         return
#     if n==2 and x==0 and y==0:
#         print("NO")
#         return
#     no,so,e,w=0,0,1,1
#     arr=['R','H']
#     ans=""
#     for i in range(n):
#         if s[i]=='N':
#             ans+=arr[no]
#             no=1-no
#         elif s[i]=='S':
#             ans+=arr[so]
#             so=1-so
#         elif s[i]=='E':
#             ans+=arr[e]
#             e=1-e
#         else:
#             ans+=arr[w]
#             w=1-w
#     print(ans)
        
# for _ in range(int(input())):
#    main()


def asquare():
    n = int(input())
    t = input()
    x = 0
    y = 0
    for i in t:
        if i == 'N':
            y += 1
        elif i == 'S':
            y -= 1
        elif i == 'W':
            x -= 1
        else:
            x += 1
    if abs(x) % 2 == 1 or abs(y) % 2 == 1:
        print("NO")
    elif n == 2 and x == 0 and y == 0:
        print("NO")
    else:
        n = s = 0
        w = e = 1
        m = ['R', 'H']
        ans = ""
        for c in t:
            if c == 'N':
                ans += m[n]
                n = 1 - n
            elif c == 'S':
                ans += m[s]
                s = 1 - s
            elif c == 'W':
                ans += m[w]
                w = 1 - w
            else:
                ans += m[e]
                e = 1 - e
        print(ans)

def main():
    t = int(input())
    for _ in range(t):
        asquare()

if __name__ == "__main__":
    main()