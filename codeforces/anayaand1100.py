import math
import sys
input=sys.stdin.readline
def main():
    s=input()
    arr=[]
    sub=[]
    for i in range(len(s)-4):
        if s[i:i+4]=="1100":
            arr.append([i,i+3])
        sub.append( s[i:i+4])
    print(arr,sub)

    q=int(input())
    for i in range(q):
        ind,v = map(int,input().split())
        if len(s)<=3:
            print("NO")
        else:
            pass
for _ in range(int(input())):
   main()