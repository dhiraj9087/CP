import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s=input().strip()
    if len(set(s))==1 and s[0]=='1':
        print(0)
        return
    print(min(len(s),2-ord(s[0])-ord(s[-1])+ord('0')+ord('0')))
    # print(ord(0))/
for _ in range(int(input())):
   main()