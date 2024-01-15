import math
import sys
import random
input=sys.stdin.readline

def main():
    s=input()
    n=len(s)
    d={}
    tar="codechef"
    # for i in s:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    # print(d)
    # ind=[]
    # for i in range(n):
    #     ind.append([s[i],i])
    # print(ind)
    # print(n)
    s=list(s)
    s.pop()
    # print(s)
    if len(s)!=len(tar):
        print(-1)
        return
    for i in range(len(s)):
        if s[i]==tar[i]:
            flag=False
            for j in range(len(s)):
                if s[i]!=tar[j] and tar[i]!=s[j]:
                    s[i],s[j]=s[j],s[i]
                    flag=True
                    break
            if flag==False:
                print(-1)
                return

    print("".join(s))



for _ in range(int(input())):
   main()