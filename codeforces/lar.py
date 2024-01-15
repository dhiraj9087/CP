import math
import sys
input=sys.stdin.readline
def lar(s):
    stack = []
    
    for char in s:
        while stack and char > stack[-1] and char not in stack:
            stack.pop()
        stack.append(char)
    
    return ''.join(stack)
def main():
    n=int(input())
    s=input().strip()
    s2=''.join(sorted(s))
    s3=lar(s)
    print(s3)
    # print(s2)
    # if s==s2:
    #     print(0)
    #     return
    # ans=0
    # for i in range(n):
    #     if s[i]==s2[i]:
    #         ans+=1
    # print(ans)

for _ in range(int(input())):
   main()