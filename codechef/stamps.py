import math
import sys
input=sys.stdin.readline
def main():
    # n=int(input())
    # s=input()
    # a=s.count('1')
    # if int(s)<=100:
    #     print(s)
    #     return
    # ans='100'
    # for i in range(n-3):
    #     ans+=0
    # print(ans)
    # # ans=""
    # # ans+='1'*(a)
    # # for i in range(n-a):
    # #     ans+='0'
    # # print(ans)
    # # ans="1"
    # # ans+='0'*(n-1)
    # # print(ans)
    n = int(input())
    s = input().strip()
    ind = -1
    flag = False

    for i in range(n - 2):
        if s[i] == '1':
            ind = i
            flag = True
            break

    if flag:
        s = '0' * n
        s = s[:ind] + '1' + s[ind + 1:]

    print(s)

    # ind = -1
    # flag = False
    # for i in range(n - 2):
    #     if s[i] == '1':
    #         ind = i
    #         flag = True
    #         break
    # if flag:
    #     for i in range(n):
    #         if i != ind:
    #             s[i] = '0'
    # ans=""
    # for i in range(len(s)):
    #     if s[i]!='\n':
    #         ans+=s[i]
    # print(ans)
    
for _ in range(int(input())):
   main()