import math
import sys
input=sys.stdin.readline
def main():
    l,n=map(int,input().split())
    if n%8==0:
        print(n)
        return
    a=str(n)
    res=""
    for i in range(len(a)-3):
        res+=a[i]
    if l==1:
        print(8)
        return
    if l==2:
        ans1 = float('inf')
        min_num1 = -1
        for i in range(10, 99):
            if i % 8 == 0:   
                c = abs(i - n)
                if c < ans1:
                    ans1 = c
                    min_num1 = i
        print(res+str(min_num1))
        return
        # if n%8<=4:
        #     while n%8!=0:
        #         n-=1
        #     print(n)
        #     return
        # if n>4:
        #     while n%8!=0:
        #         n+=1
        #     print(n)
        #     return
    
    # s=a-a[-3:]
    # digi=a[-3:]
    # # print(digi)
    # if int(digi)%8==0:
    #     print(n)
    #     return
    # ans=''
    # for i in range(11):
    #     q=str(i)+digi[1:]
    #     if int(q)%8==0:
    #         ans=q
    #         break
    # for i in range(10):
    #     q=digi[0]+str(i)+digi[2]
    #     if int(q)%8==0:
    #         ans=q
    #         break
    # for i in range(10):
    #     q=digi[:2]+str(i)
    #     if int(q)%8==0:
    #         ans=q
    #         break
    # # print(ans)
    
    # print(int(res+ans))
    digi=a[-3:]
    ans=float('inf')
    min_num=-1
    for i in range(100,999):
        if i%8==0:
            w=str(i)
            c=0
            # for j in range(3):
            #     a1=int(w[j])
            #     a2=int(digi[j])
            #     c+=abs(a1-a2)
            c=abs(i-int(digi))
            if c < ans:
                ans = c
                min_num = i
    print(res+str(min_num))
    
    
for _ in range(int(input())):
   main()

