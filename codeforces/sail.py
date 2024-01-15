# t,sx,sy,ex,ey=map(int,input().split())
# s=input()
# q,c,flag,flag1="",0,0,0
# a=ex-sx
# b=ey-sy
# # print(a,b)
# if a<0:
#     q=q+"W"*abs(a)
#     if q.count("W")==s.count("W"):
#         flag+=1
#         # print("1")
# if a>0:
#     q=q+"E"*abs(a)
#     if q.count("E")==s.count("E"):
#         flag+=1
#         # print("2")
# if b<0:
#     q=q+"S"*abs(b)
#     if q.count("S")==s.count("S"):
#         flag1+=1
#         # print("3")
# if b>0:
#     q=q+"N"*abs(b)
#     if q.count("N")==s.count("N"):
#         flag1+=1
#         # print("4")
# # print(q,flag)
# # d1=[]
# # for i in q:
# #     d1.append(q.count(i))
# # print(d1)
# # d={}
# # for i in s:
# #     d[i]=s.count(i)
# # print(d)
# # print(flag,flag1)
# if flag>0 and flag1>0:
#     print((a+b)*2)
# else:
#     print("-1")



# import sys

t, sx, sy, ex, ey= map(int,input().split())
time=-1
wind =input()

for i in range(t):
    if wind[i] == 'E' and sx < ex:
        sx += 1
    elif wind[i] == 'S' and sy > ey:
        sy -= 1
    elif wind[i] == 'W' and sx > ex:
        sx -= 1
    elif wind[i] == 'N' and sy < ey:
        sy += 1
    if sx == ex and sy == ey:
        time = i + 1
        break

print(time)











# # If the wind blows to the east, the boat will move to (x + 1, y).
# # If the wind blows to the south, the boat will move to (x, y - 1).
# # If the wind blows to the west, the boat will move to (x - 1, y).
# # If the wind blows to the north, the boat will move to (x, y + 1).