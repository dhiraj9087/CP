import math
a,b,c=map(int,input().split())
x=math.sqrt((a*b)//c)
y=math.sqrt((b*c)//a)
z=math.sqrt((a*c)//b)
print(int(4*(x+y+z)))