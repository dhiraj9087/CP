a=[]
for i in range((int(input()))):
    array = list(map(int,input().split()))
    a.append(array)
# print(a)
s=0
d=0
q=0
for array in a:
    s+=array[0]
    d+=array[1]
    q+=array[2]
if(s==0 and d==0 and q==0):
    print("YES")
else:
    print("NO")
#print(s)
