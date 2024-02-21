import math
import sys
input=sys.stdin.readline
def main():
    n,m,x0,y0,l=map(int,input().split())
    if l==1:
        print(n*m)
        return
    ru,rd,cr,cl=0,0,0,0
    ru=x0-1
    rd=n-x0
    cr=m-y0
    cl=y0-1
    ans=0
    ru//=l
    rd//=l
    cr//=l
    cl//=l
    # print(ru,rd,cr,cl)
    ans+=(ru+rd)+(cl+cr)+(ru+rd)*(cl+cr)
    # if ru>=l:
    #     ans*= ru//l
    # if rd>=l:
    #     ans*= rd//l
    # if cr>=l:
    #     ans*= cr//l
    # if cl>=l:
    #     ans*= cl//l
    # ans+=(ru//l)*(rd//l)*(cr//l)*(cl//l)
    print(ans+1)
for _ in range(int(input())):
   main()