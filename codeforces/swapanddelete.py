import math
import sys
input=sys.stdin.readline
def main():
    s = input().strip()
    a=[]
    n = len(s)
    ones, zeros = 0, 0

    for i in s:
        if i == '1':
            ones += 1
        else:
            zeros += 1

    for i in range(len(s)):
        if s[i] == '0':
            if ones > 0:
                a.append('1')
                ones -= 1
        else:
            if zeros > 0:
                a.append('0')
                zeros -= 1
        # a += 1

    ind = -1
    for i in range(len(a)):
        if a[i] == s[i]:
            ind = i
            break

    if ind == -1:
        print(n - len(a))
    else:
        print(n - ind)

    # print(zero,one,abs(zero-one))
    
for _ in range(int(input())):
   main()