# cook your dish here
y=int(input())
for i in range(y):
    a,b,c,d=map(int,input().split())
    if((b+d)>=a and c>=a):
        print("YES")
        
          
    else:
        print("NO")
