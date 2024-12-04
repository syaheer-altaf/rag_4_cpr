import heapq

with open("matrix.txt", "r") as file:
    matrix = [list(map(int, line.split(','))) for line in file]

rows = len(matrix)
cols = len(matrix[0])

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distances = [[float('inf')] * cols for _ in range(rows)]
distances[0][0] = matrix[0][0]

priority_queue = [(matrix[0][0], 0, 0)]

while priority_queue:
    current_dist, x, y = heapq.heappop(priority_queue)
    if current_dist > distances[x][y]:
        continue
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            new_dist = current_dist + matrix[nx][ny]
            if new_dist < distances[nx][ny]:
                distances[nx][ny] = new_dist
                heapq.heappush(priority_queue, (new_dist, nx, ny))

print(distances[-1][-1])