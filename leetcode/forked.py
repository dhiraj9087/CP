import math
import sys
input=sys.stdin.readline
def main():
    a,b=map(int,input().split())
    xk,yk=map(int,input().split())
    xq,yq=map(int,input().split())
    s1,s2=set(),set()
    s1.add((xk+a,yk+b))
    s1.add((xk+b,yk+a))
    s1.add((xk-a,yk-b))
    s1.add((xk-b,yk-a))
    s1.add((xk+a,yk-b))
    s1.add((xk+b,yk-a))
    s1.add((xk-a,yk+b))
    s1.add((xk-b,yk+a))
    s2.add((xq-a,yq-b))
    s2.add((xq-b,yq-a))
    s2.add((xq-b,yq-a))
    s2.add((xq-b,yq-a))
    s2.add((xq-a,yq+b))
    s2.add((xq-b,yq+a))
    s2.add((xq-b,yq+a))
    s2.add((xq-b,yq+a))
    # x_1,y_1=xk+a,yk+b
    # x_2,y_2=xk+b,yk+a
    # x_11,y_11=xq-a,yq-b
    # x_22,y_22=xq-b,yq-a
    # q,w=[[abs(x_1),abs(y_1)],[abs(x_2),abs(y_2)]],[[abs(x_11),abs(y_11)],[abs(x_22),abs(y_22)]]
    # q=set(q)
    # q=list(q)
    # w=set(w)
    # w=list(w)
    ans=0
    for i in s1:
        if i in s2:
            ans+=1
    # for i in q:
    #     if i in w:
    #         ans+=1
    print(ans)
    # print([abs(x_1),abs(y_1)],[abs(x_2),abs(y_2)],[abs(x_11),abs(y_11)],[abs(x_22),abs(y_22)])
for _ in range(int(input())):
   main()