ans=[]
while True:
    a=int(input())
    if a<0:
        break
    else:
        if a<100:
            ans.append(a)
# print(max(ans))
if len(ans)==0:
    print(0)
else:
    print(max(ans))
