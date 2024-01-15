def main():
    n = 3
    edges = [[0,1],[1,2]]
    # n = 4
    # edges = [[0,2],[1,3],[1,2]]
    a=[0]*n
    for i in edges:
        a[i[1]]=1
    ans=0
    for i in range(len(a)):
        if a[i]==0:
            ans+=1
    if ans>1:
        return -1
    for i in range(len(a)):
        if a[i]==0:
            return i
print(main())