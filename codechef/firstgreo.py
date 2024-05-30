import math
import sys
input=sys.stdin.readline
def main():
    s=input().strip()
    l,r,u,d=s[0],s[1],s[2],s[3]
    c=s.count('1')
    if c==1:
        print(11)
        return
    if c==3:
        print(231)
        return
    if c==4:
        print(441)
        return
    if (l=='1' and r=='1' and u=='0' and d=='0') or (l=='0' and r=='0' and u=='1' and d=='1'):
        print(21)
        return
    print(121)

    
for _ in range(int(input())):
   main()