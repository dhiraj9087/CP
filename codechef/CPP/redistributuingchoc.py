# cook your dish here
for i in range((int(input()))):
    x,y,z=map(int,input().split())
    if(x!=y and y!=z and x!=z):
        print("YES")
        
    elif(x==1 and y==1 and z==1):
        print("NO")
    elif(x==y and y==z and z==x):
        print("YES")
        
    elif(x==y or y==z or z==x):
        list=[x,y,z]
        if((max(list)-min(list))>2):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    # list=[x,y,z]
    # print(list)