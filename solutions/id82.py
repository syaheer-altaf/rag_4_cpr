with open("matrix.txt", "r") as file:
    matrix = [list(map(int, line.split(','))) for line in file]

rows = len(matrix)
cols = len(matrix[0])

for j in range(1, cols):
    dp = [row[j] + matrix[row_idx][j - 1] for row_idx, row in enumerate(matrix)]
    for i in range(1, rows):
        dp[i] = min(dp[i], dp[i - 1] + matrix[i][j])
    for i in range(rows - 2, -1, -1):
        dp[i] = min(dp[i], dp[i + 1] + matrix[i][j])
    for i in range(rows):
        matrix[i][j] = dp[i]

print(min(row[-1] for row in matrix))