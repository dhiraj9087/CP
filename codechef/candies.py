# cook your dish here
y=int(input())
for i in range(y):
    #l=[]
    c=0
    p=int(input())
    #for i in range(n):
    n=list(map(int,input().strip().split()))
        #l.append(ele)
        
    n.sort()
    for i in range(len(n)):
        if(n[i]==n[i+1]):
            c=c+1

                
        
       
        
    if(c>=3):
        print("NO")
    else:
        print("YES")