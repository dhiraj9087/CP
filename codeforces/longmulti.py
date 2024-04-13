import math
import sys
input=sys.stdin.readline
def main():
    a=input().strip()
    b=input().strip()
    # 3582
    # 3916 14027112
    # 3912
    # 3586 
    maxi=-1
    mini=float('inf')
    ind=-1
    for i in range(len(a)):
        if int(a[i])!=int(b[i]):
            maxi=max(int(a[i]),int(b[i]))
            mini=min(int(a[i]),int(b[i]))
            ind=i
            break
    num1,num2="",""
    for i in range(len(a)):
        if i<ind:
            num1+=a[i]
            num2+=b[i]
        elif i==ind:
            num1+=str(maxi)
            num2+=str(mini)
        else:
            if int(a[i])>int(b[i]):
                num1+=b[i]
                num2+=a[i]
            else:
                num1+=a[i]
                num2+=b[i]
    # print(maxi,ind,num1,num2)
    print(int(num1))
    print(int(num2))

for _ in range(int(input())):
   main()