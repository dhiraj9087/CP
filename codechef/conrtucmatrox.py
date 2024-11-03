import math
import sys
input=sys.stdin.readline
def create_minimal_matrix(n, m):
    # Step 1: Initialize the matrix filled with 2s
    matrix = [[2 for _ in range(m)] for _ in range(n)]
    
    # Step 2: Place 3s in a way that each row and column has at least one 3
    for i in range(n):
        if i % 2 == 0:
            matrix[i][0] = 3  # Place 3 in the first column for even rows
        else:
            matrix[i][1] = 3  # Place 3 in the second column for odd rows
            
    return matrix
def main():
    n, m = map(int, input().split())
    a = [[2 for _ in range(m)] for _ in range(n)]
    if n == 2 and m == 3:
        a = [[2, 3, 3],
             [3, 2, 2]]
    else:
        if n==m:
            for i in range(n):
                for j in range(m):
                    a[i][i] = 3
        else:
            if n > m:
                for i in range(m):
                    a[i][i] = 3  
                for i in range(m, n):
                    a[i][0] = 3  
            else:
                for i in range(n):
                    a[i][i] = 3  
                for i in range(n, m):
                    a[0][i] = 3
        # if n == 4 and m == 4:
        #     a[0][2] = 3 
        #     a[1][0] = 3  
        #     a[2][1] = 3  
        #     a[3][3] = 3 
        # else:
        #     a[0][0] = 3  
        #     if m > 1:
        #         a[1][1] = 3  
    # ans = create_minimal_matrix(n, m)
    # print(ans)
    for row in a:
        print(" ".join(map(str, row)))
for _ in range(int(input())):
   main()