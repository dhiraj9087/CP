import math
import sys
input=sys.stdin.readline
def main():
    s,n=input().split()
    n=int(n)
    arr=[0]*len(s)
    w,r,c=0,0,0
    for i in range(len(s)):
        if s[i]=='R':
            r+=1
        elif s[i]=='W':
            w+=1
        if r==w:
            arr[i]=1
            c+=1
            r=0
            w=0
    if c>=n:
        print(1)
        return
    print(0)
    # print(arr)

# for _ in range(int(input())):
main()