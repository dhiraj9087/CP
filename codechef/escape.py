import math
import sys
input=sys.stdin.readline
def main():
    n,k,h=map(int,input().split())
    a = 1
    b = 1
    temp = 0
    while a<=n:
        if a<h:
            if (a*k - b*(k-1))>=h:
                while (a*k - b*(k-1))>=h:
                    b+=1
                temp += b-1

            else:
                a+=1
        else:
            temp += n
            a+=1


    print(temp)


    # ans=0
    # c=0
    # if n<k and n<h:
    #     print(0)
    #     return
    # for i in range(h,n+1):  
    #     c+=1
    # ans+=(c*n)
    # # print(ans)
    # if h%k==0:
    #     rem=h//k
    # else:
    #     rem =( h//k ) + 1
    # for i in range(1,h):
    #     ans += max(0,(i-rem))
    # for i in range(1,h//k):
    #     ans += ((h//k -i) * (k-1))
    # print(ans)
for _ in range(int(input())):
   main()