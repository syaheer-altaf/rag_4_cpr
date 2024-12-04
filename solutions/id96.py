def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def extract_top_left(board):
    return board[0][0] * 100 + board[0][1] * 10 + board[0][2]

def solve_sudoku_puzzles(file_path):
    total = 0
    with open(file_path, 'r') as f:
        puzzles = f.read().splitlines()
        for i in range(0, len(puzzles), 10):
            board = []
            for j in range(1, 10):
                board.append([int(digit) for digit in puzzles[i + j]])
            solve_sudoku(board)
            total += extract_top_left(board)
    return total

print(solve_sudoku_puzzles("sudoku.txt"))