import math
import sys
input=sys.stdin.readline
def main():
   geek=[1,1]
   if geek==[1,1]:
      print("YES")
    # l,r=map(int,input().split())
    # # print(math.gcd(895895, 895895 ))
    # if r<=3:
    #     print(-1)
    #     return
    # if l!=r:
    #     if l%2==0 and l!=2:
    #         print(l//2,l//2)
    #         return
    #     if r%2==0:
    #         print(r//2,r//2)
    #         return
    #     print((r-1)//2,(r-1)//2)
    #     return
    # else:
    #     if l%2==0:
    #         print(l//2,l//2)
    #         return
    #     h=l**(0.5)+1
    #     p=3
    #     j=0
    #     while(p<=h):
    #       if(l%p==0 and (l-p)%p==0):
    #         print(int(p),int(l-p))
    #         j=1
    #         break
    #       else:
    #         p=p+2
    #     if(j==0):
    #       print("-1")
    #       return
        
    # if r-l>=2 and l>1:
    #     if l%2==0:
    #         print(l,2)
    #     else:
    #         print(l-1,2)
    # elif l==r:
    #     print(l//2,l//2)
    # elif r-l==1 and l>1:
    #     if l%2==0:
    #         print(l-2,2)
    #     else:
    #         print(l-1,2)
    # else:
    #     print('-1')
for _ in range(int(input())):
   main()