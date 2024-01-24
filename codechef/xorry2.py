import math
import sys
input=sys.stdin.readline
def intToBin(n):
    x = ""
    while n != 0:
        if n & 1:
            x += '1'
        else:
            x += '0'
        n >>= 1
    return x[::-1]
def main():
    n=int(input())
    s=bin(n)[2:]
    # s=intToBin(n)
    # print(s)
    # flag=False
    if s.count('1')==1:
        print(1)
        return
    # if '11' in s:
    #     flag=True
    # if flag==False:
    #     print(1)
    #     return
    val=0
    for i in range(len(s)):
        if s[i]=='1':
            val+=1
            if val==2:
                ind=i+1
                break
                
    # ind=0
    # # if flag==True:
    # ptr = 0
    # pos = 0
    # # a='11'
    # for i in range(len(s)):
    #     if s[i] == '1':
    #         ptr += 1
    #         if ptr == 2:
    #             pos = i + 1
    #             break
    c=0
    if val<=1:
        print(1)
        return
    
    for i in range(ind,len(s)):
        if s[i]=='0':
            c+=1
    print(2**c)
    
    # ptr,pos=0,0
    # a='11'
    # for i in range(len(s)):
    #     if s[i]==a[ptr]:
    #         ptr+=1
    #         if ptr==2:
    #             pos = i+1
    #             break
    # if ptr <= 1:
    #     print(1)
    #     return
    # c=0
    # for i in range(pos,len(s)):
    #     if s[i]=='0':
    #         c+=1
    # print(2**c)

for _ in range(int(input())):
   main()