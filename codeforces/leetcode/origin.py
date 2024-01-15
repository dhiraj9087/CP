moves ="_______"
l,r,a=0,0,0
for i in moves:
    if i=='L':
        l+=1
    elif i=="R":
        r+=1
    else:
        a+=1
if l>=r:
    print(l+a-r)
elif r>l:
    print(r+a-l)

