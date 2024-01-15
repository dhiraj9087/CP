ranked_count = int(input().strip())

r=list(map(int, input().rstrip().split()))

player_count = int(input().strip())

p=list(map(int, input().rstrip().split()))

# r=set(r)
# #print(r)
# a=list(r)
# a.sort()
# print(a)
# for i in range(player_count):
#     for j in range(len(a)):
#         if(a[j]>p[i]):
#             a.insert(i,p[i])
#             #break
#             #print(ranked_count-1)
#             print(a)
#             break
#         else:
#             continue
a=[]
r=list(set(r))
a=r+p
a.sort()
a=list(set(a))
a.sort(reverse=True)
print(a)

# for i in range(len(a)):
#     # for j in range(len(a)):
#     j=0
#     while(j<len(a)):
#         if(p[i]==a[j]):
#             if(j==ranked_count):
#                 print(ranked_count-1)
#             elif(j==0):
#                 print('1')
#             else:
#                 print(j)
#             j+=1
            
    #print(p[i])
#print(len(p))
# result=[a.index(i) for i in p]
# print(result)
for i in p:
    index=a.index(i)
    if(index==ranked_count):
        print(ranked_count-1)
    elif(index==0):
        print('1')
    else:
        print(index)