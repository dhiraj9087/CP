import math
import sys
input=sys.stdin.readline
def main():
    n,c,d=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    arr=[]
    # print(a)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    matrix[0][0] = a[0]
    arr.append(matrix[0][0])
   
    for i in range(1, n):
        matrix[0][i] = matrix[0][i-1] + d
        matrix[i][0] = matrix[i-1][0] + c
        arr.append(matrix[0][i])
        arr.append(matrix[i][0] )

    for i in range(1, n):
        for j in range(1, n):
            matrix[i][j] = min(matrix[i-1][j] + c, matrix[i][j-1] + d)
            arr.append(matrix[i][j])
    # print(arr)
    arr.sort()
    if arr==a:
        print("YES")
        return
    print("NO")
for _ in range(int(input())):
   main()