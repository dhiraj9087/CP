from collections import *
grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
# grid = [[1,2,2],[1,1,0],[0,1,0]]
# grid = [[0,1,0],[2,1,0],[0,2,0]]
grid = [[0,2,0,1,2],[0,0,0,1,2],[2,0,2,1,0],[2,0,2,2,0],[1,2,2,0,1]]
# 0 2 0 1 2
# 0 0 0 1 2
# 2 0 2 1 0
# 2 0 2 2 0
# 1 2 2 0 1






n = len(grid)
rows = len(grid)
cols = len(grid[0])

tl = [grid[i][i] for i in range(min(rows//2+1, cols))]
ind1=[[i,i] for i in range(min(rows//2+1, cols))]
tr = [grid[i][cols - i - 1] for i in range(min(rows//2, cols))]
ind2=[[i,cols - i - 1] for i in range(min(rows//2+1, cols))]
ce = [grid[i][cols // 2] for i in range(rows // 2+1, rows)]
ind3=[[i,cols // 2] for i in range(rows // 2+1, rows)]
a=tl+tr+ce
print(a)
d=Counter(a)
maxi=float('-inf')
print(d)
ele=0
for i,j in d.items():
    if j>maxi:
        maxi=j
        ele=i
print(maxi,ele)
a_ind=ind1+ind2+ind3
rem=[]
for i in range(n):
    for j in range(n):
        if [i,j] not in a_ind:
            rem.append(grid[i][j])
d2=Counter(rem)
maxi2=float('-inf')
ele2=0
for i,j in d2.items():
    if j>maxi2:
        maxi2=j
        ele2=i
print(d2)
print(maxi2,ele2)
y_make=-1
outer=-1
ans=0
if ele!=ele2:
    for i in a:
        if i!=ele:
            ans+=1
    for i in rem:
        if i!=ele2:
            ans+=1
    print(ans)
else:
    if maxi>=maxi2:
        y_make=ele
        for i in range(len(a)):
            if a[i]!=y_make:
                ans+=1
        for i,j in d2.items():
            if j==maxi2:
                outer=i
                break
        for i in range(len(rem)):
            if rem[i]!=outer:
                ans+=1
        
    else:
        for i,j in d.items():
            if j<maxi:
                y_make=i
                break
        for i in range(len(a)):
            if a[i]!=y_make:
                ans+=1
        for i,j in d2.items():
            if j==maxi2:
                outer=i
                break
        for i in range(len(rem)):
            if rem[i]!=outer:
                ans+=1
print(a,ele,ele2,rem,y_make,outer,maxi,maxi2)
print(ans)