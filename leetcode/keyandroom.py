def main():
    # rooms = [[1],[2],[3],[]]
    rooms = [[1,3],[3,0,1],[2],[0]]
    rooms = [[6,7,8],[5,4,9],[],[8],[4],[],[1,9,2,3],[7],[6,5],[2,3,1]]
    n=len(rooms)
    d={i:0 for i in range(n)}
    d[0]=1
    # print(d)
    # for i in range(n):
    #     for j in range(len(rooms[i])):
    #         print(d[i][j])
    for i in range(n):
        for j in range(len(rooms[i])):
            if d[i]==1:
                d[rooms[i][j]]=1
    print(d)
    for i,j in d.items():
        if j==0:
            return False
    return True
print(main())