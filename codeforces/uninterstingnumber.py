import math
import sys
input=sys.stdin.readline

def main():
    s=input().strip()
    c2,c3,add=0,0,0
    for i in s:
        add+=int(i)
        if i=='2':
            c2+=1
        elif i=='3':
            c3+=1
    if add%9==0:
        print("YES")
        return
    ans=False
    for i in range(min(10,c2)+1):
        for j in range(min(3,c3)+1):
            if (add+2*i+6*j)%9==0:
                ans=True
                break
                
        if ans:
            break
    if ans:
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
   main()