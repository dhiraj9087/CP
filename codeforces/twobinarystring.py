import math
import sys
input=sys.stdin.readline
def main():
    a=input()
    b=input()
    if a==b:
        print("YES")
        return
    one=[]
    two=[]
    for i in range(1,len(a)):
        if a[i]=='1' and a[i-1]=='0':
            one.append(i)
        if b[i]=='1' and b[i-1]=='0':
            two.append(i)
    for i in one:
        if i in two:
            print("YES")
            return
    print("NO")
for _ in range(int(input())):
   main()