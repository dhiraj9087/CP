import math
import sys
import decimal
input=sys.stdin.readline
def main():
    n=decimal.Decimal(input())
    val=decimal.Decimal(int(decimal.Decimal.sqrt(n)))
    # print(val//2)
    # print(val)
    if n%2==1:
        val+=1
        # print(math.ceil(val//2))
    # else:
    # print(val)
    print(val//2)
    
for _ in range(int(input())):
   main()

   