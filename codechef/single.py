import math
for i in range((int(input()))):
    h,x,y=map(int,input().split())
    if h==y:
        print("1")
    else:
        # print(h//x , (h-y)//x+1)
        print(math.ceil((h-y)/x)+1)