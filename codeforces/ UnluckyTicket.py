n,a=int(input()),input()
half1,half2,c,q=[],[],0,0
for i in range(len(a)):
    if i<n:half1.append(int(a[i])) 
    else:half2.append(int(a[i]))
half1.sort(),half2.sort()
for i in range(len(half1)):
    if half1[i]>half2[i]:c+=1
    elif half1[i]<half2[i]:q+=1
if c==n or q==n:print("YES")
else:print("NO")