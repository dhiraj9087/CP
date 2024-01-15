import math
import sys
input=sys.stdin.readline
def main():
    # n=list(input())
    # a=[]
    # for i in range(len(n)-1):
    #     a.append(n[i])
    # # print(a)
    # for i in range(len(a)-1,-1,-1):
    #     if int(a[i])>=5:
    #         a[i-1]=str(int(a[i-1])+1)
    # if int(a[0])>=5:
    #     a=['1']+a
    # print(a)

    # s=''
    # if len(n)==1:
    #     if int(n)>=5:
    #         print(10)
    #         return
    #     else:
    #         print(0)
    #         return
    # # c=0
    # # print(n)
    # for i in range(len(a)-2,-1,-1):
    #     if int(a[i+1])  >=5:
    #         a[i]=str(int(i)+1)
    #         a[i+1]=0
        
    # print(a)
    s = input().strip()
    size = len(s)
    
    for i in range(size - 1, 0, -1):
        if int(s[i]) >= 5:
            s = s[:i] + str(int(s[i-1]) + 1) + s[i+1:]
    
    if int(s[0]) >= 5:
        s = '1' + s
    
    ind = size + 2
    for i in range(len(s)):
        if int(s[i]) >= 5:
            ind = i
            break
    
    s = s[:ind] + '0' * (size - ind)
    print(s)
    




    
for _ in range(int(input())):
    main()