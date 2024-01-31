import math
import sys
input=sys.stdin.readline
def main():
    a,b,r=map(int,input().split())
    x=0
    flag=False
    flag2=False
    for i in range(31,-1,-1):
        bit_a = (a >> i) & 1
        bit_b = (b >> i) & 1
        if bit_a == bit_b:
            x |= (bit_a << i)
        else:
            if a>b:
                if flag==False:
                    x |= (bit_b<<i)
                    flag=True
                else:
                    x |= (bit_a<<i)
            else:
                if flag2==False:
                    x |= (bit_a<<i)
                    flag2=True
                else:
                    x |= (bit_b<<i)
            # if a>b and flag==False:
            #     x |= (bit_b << i)
            #     flag=True
            # elif b>a and flag2==False:
            #     x |= (bit_a << i)
            #     flag2=True
            # s = min(bit_a, bit_b)
            # x |= (s << i)
    print(abs((a^x) - (b^x)))
    print(a^x,b^x)
    print(min(x,r))
for _ in range(int(input())):
   main()