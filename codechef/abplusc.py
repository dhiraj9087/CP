import math
# for i in range((int(input()))):
#     n=int(input())
#     if n==1:print('-1')
#     elif n==2: print(1,1,1)
#     else:
#         if math.sqrt(n-1) * math.sqrt(n-1) == n+1:
#             print(int(math.sqrt(n-1)),int(math.sqrt(n-1)),1)
#         else:
#             largest_square = math.floor(math.sqrt(n-1)) ** 2
#             a=int(math.sqrt(largest_square))
#             b=int(math.sqrt(largest_square))
#             c=(n-(largest_square))
#             print(a,b,c)
# for i in range(int(input())):
#     x=int(input())
#     a=0;
#     b=0;
#     c=0;
#     if x==1:
#         print(-1);
#     elif x<1000000:
#         print(x-1,1,1);
#     else:
#         a=1000000;
#         if x%1000000==0:
#             b=1000000;
#         else:
#             b=x%(1000000);
#         c=(x-b)//a;
#         print(c,a,b)
            
import math

for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print('-1')
    elif n == 2:
        print('1 1 1')
    else:
        # k = int(math.sqrt(n-1))
        # if (n-1) % k == 0 and (n-1)//k + k == n+1:
        #     print(k, k, 1)
        # else:
        #     largest_square = k*k
        #     a = int(math.sqrt(largest_square))
        #     b = int(math.sqrt(largest_square))
        #     c = n - largest_square
        #     print(a, b, c)
        if n<=10**6+1:
            print(1,1,n-1)
        else:
            m=10**6
            c = n % m
            if c:
                print(m,n//m,c)
            else:
                l = n - m
                print(n//m-1,m,m)
