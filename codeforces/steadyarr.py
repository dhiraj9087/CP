
N=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr)
s,c=0,0
q=set()
for i in range(len(arr)):
    s+=arr[i]
    print(s,q)
    if s in q:
        c+=1
        break
    q.add(s)
    
if c>0:
    print("YES")
else:
    print("NO")





