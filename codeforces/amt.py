def min_operations(n, m, matrix, A, B):
    result = [[0] * m for _ in range(n)]

    for i in range(n):
        result[i][:A[i]] = [1] * A[i]

    for j in range(m):
        for i in range(B[j]):
            result[i][j] = 1

    operations = 0

    for i in range(n):
        for j in range(m):
            if result[i][j] != matrix[i][j]:
                operations += 1

    return operations if operations > 0 else -1

# Input reading
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Calculate and print the result
result = min_operations(n, m, matrix, A, B)
print(result)

 