R, C = tuple(map(int, input().split()))

matrix = [list(map(int, input().split())), []]
matrix[1] = list(map(int, input().split()))

print(matrix[R-1][C-1])