import math
import sys
input=sys.stdin.readline
def digit_sum(number):
    s = 0
    while number > 0:
        digit = number % 10
        s += digit
        number //= 10
    return s
def main():
    n=int(input())
    a=list(map(int,input().split()))
    odd,even=[],[]
    for i in range(n):
        if len(str(a[i]))%2==0:
            even.append(a[i])
        else:
            odd.append(a[i])
    # print(even,odd)
    tar=""
    tar_1,tar_2="",""
    ans=0
    for i in range(len(even)):
        for j in range(len(even)):
            tar=str(even[i])+str(even[j])
            tar_1=tar[:len(tar)//2]
            tar_2=tar[len(tar)//2:]
            # print(tar,tar_1,tar_2)
            if digit_sum(int(tar_1))==digit_sum(int(tar_2)):
                ans+=2
    for i in range(len(odd)):
        for j in range(len(odd)):
            tar=str(odd[i])+str(odd[j])
            tar_1=tar[:len(tar)//2]
            tar_2=tar[len(tar)//2:]
            # print(tar,tar_1,tar_2)
            if digit_sum(int(tar_1))==digit_sum(int(tar_2)):
                ans+=2
    print(ans//2)
# for _ in range(int(input())):
main()