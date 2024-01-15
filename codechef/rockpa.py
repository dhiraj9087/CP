import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    s1=input()
    s2=input()
    chef,chefina=0,0
    for i in range(n):
        if s1[i]=='R' and s2[i]=='S':
            chef+=1
        elif s1[i]=='S' and s2[i]=='P':
            chef+=1
        elif s1[i]=='P' and s2[i]=='R':
            chef+=1
        elif s1[i]==s2[i]:
            pass
        else:
            chefina+=1
    # print(chef,chefina)
    if chef<=chefina:
        print((chefina-chef)//2 + 1)
        return
    print(0)
for _ in range(int(input())):
   main()