import math
import sys
input=sys.stdin.readline
def main():
    n=int(input())
    num=1
    rem=[]
    if n%62==0:
        print(1)
        return
    while num<n:
        num=num*62
    num = num//62
    # print(num)
    while True:
        num=num*62
        if num>n:
            num = num // 62
            for i in range(1,63):
                if num*i>n:
                    num = num *(i-1)
                    rem.append(i-1)
                    break
        break
    # print(num,rem) 
    left = n-num
    for i in range(1,63):
        if 62 * i == left:
            num = num + (62*i)
            rem.append(1)
            break
        if 62 * i > left:
            num = num + (62*(i-1))
            rem.append(i-1)
            break
    if num!=n:
        rem.append(n-num)
    # print(num,rem)
    ans=""
    for i in rem:
        if 0<=i<=9:
            ans+=(str(i))
        elif 10<=i<=35:
            ans+=chr(i - 10 + ord('A'))
        elif 36<=i<=61:
            ans+=chr(i - 36 + ord('a'))
    print(ans)
for _ in range(int(input())):
   main()