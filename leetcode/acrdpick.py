cards=[95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]
# cards = [3,4,2,3,4,7]
# cards = [1,0,5,3]

a=[]
mini=float('inf')
d={}
for i,j in enumerate(cards):
    if j in d:
        d[j]=i-d[j]+1
        a.append(d[j])
    else:
        d[j]=i
    # print(i,j)
print(d,a)
print(max(a))



# return -1