# cook your dish here
y=int(input())
for y in range(y):
    a,b,c=map(int,input().split())
    d=(b//c)
    if(b<=c):
        print(a)
    elif(b%c==0):
        print((a*d))
    elif(b>c):
        print((a*(d+1)))
        
    
    