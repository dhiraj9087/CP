import sys
input=sys.stdin.readline

def main():
    n=int(input())
    a=[]
    ind,qua=-1,-1
    for i in range(n):
        x,y=map(int,input().split())
        if x<=10 and y>qua:
            qua=y
            ind=i
    print(ind+1)
            
        
for _ in range(int(input())):
    main()
    