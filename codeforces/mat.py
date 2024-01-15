import math
import sys
input=sys.stdin.readline
def main():
    res=0
    ans=[]
    b=[]
    for i in range(1,11):
        a=input()
        n=len(a)-1
        if a[n]!='\n':
            ans.append(a[:])
        else:
            ans.append(a[:n])
    for i in range(10):
        for j in range(10):
            # if i==0 or j==9 or i==9 or j==0:
            #     cnt=a.count('X')
            #     print(cnt)
            #     res=cnt*1
            if ans[i][j]=='X':
                b.append((i,j))
    # print(b)
    for i in range(len(b)):
        c1= b[i][0]
        c2 = b[i][1]
        if c1==0 or c1==9 or c2==0 or c2==9:
            res+=1
        elif c1==1 or c1==8 or c2==1 or c2==8:
            res+=2
        elif c1==2 or c1==7 or c2==2 or c2==7:
            res+=3
        elif c1==3 or c1==6 or c2==3 or c2==6:
            res+=4
        else:
            res+=5
    print(res)
        # if i==1 or i==10:
        #     c=a.count('X')
        #     ans = c*1
        # elif i==2 or i==9:
        #     c=a.count('X')
        #     ans = c*2
        # elif i==3 or i==8:
        #     c=a.count('X')
        #     ans = c*3
        #     # print(a,c,ans)
        # elif i==4 or i==7:
        #     c=a.count('X')
        #     ans = c*4
        # elif i==5 or i==6:
        #     c=a.count('X')
        #     ans = c*5
        # print(ans)
    
for _ in range(int(input())):
   main()