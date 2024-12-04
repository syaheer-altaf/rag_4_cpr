with open("matrix.txt", "r") as file:
    matrix = [list(map(int, line.split(','))) for line in file]

rows = len(matrix)
cols = len(matrix[0])

for i in range(rows - 2, -1, -1):
    matrix[i][cols - 1] += matrix[i + 1][cols - 1]

for j in range(cols - 2, -1, -1):
    matrix[rows - 1][j] += matrix[rows - 1][j + 1]

for i in range(rows - 2, -1, -1):
    for j in range(cols - 2, -1, -1):
        matrix[i][j] += min(matrix[i + 1][j], matrix[i][j + 1])

print(matrix[0][0])