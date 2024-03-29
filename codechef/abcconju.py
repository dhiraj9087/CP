import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    a=input().strip()
    b=input().strip()
    arr=[]
    for i in range(n):
        if (a[i]=='b' and b[i]!='b') or (a[i]!='b' and b[i]=='b'):
            print("No")
            return
    ind=0
    while ind<n:
        l,p=0,0
        while ind<n:
            if b[ind]=='c' and a[ind]=='a':
                l+=1
            if b[ind]=='a' and a[ind]=='c':
                p+=1
            if a[ind]=='b':
                ind+=1
                break
            ind+=1
        if l or p:
            arr.append([l,p])
    # print(arr,)
    l,p=0,0
    for i in range(len(arr)):
        p+=(arr[i][1])
        if p>l:
            print("No")
            return
        l+=arr[i][0]
    if l==p:
        print("Yes")
        return
    print("No")
for _ in range(int(input())):
   main()