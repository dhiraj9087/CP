import math
import sys
input=sys.stdin.readline
def main():
    s=input().strip()
    digits = [int(i) for i in s]
    for i in range(1,len(s)):
        ind=i
        while ind>=1 and digits[ind]>0 and digits[ind] > digits[ind-1]+1:
            val = digits[ind]
            digits[ind] = digits[ind - 1]
            digits[ind - 1] = val - 1
            if ind>1:
                ind-=1
            else:
                break
    res = ''.join(map(str, digits))
    print(res)

for _ in range(int(input())):
   main()