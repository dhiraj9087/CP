for i in range((int(input()))):
    x,y=map(int,input().split())
    if(x<y):
        if(y-x==1 and y%2==0):
            print("CHEF")
        else:
            print("CHEFINA")
    if(x>y):
        if(x-y ==1 and x%2!=0):
            print("CHEFINA")
        else:
            print("CHEF")
    if(x==y):
        if(x%2==0):
            print("CHEFINA")
        else:
            print("CHEf")
    
        

        