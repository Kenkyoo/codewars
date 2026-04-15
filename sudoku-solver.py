def sudoku(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(puzzle, row, col, num):
                        puzzle[row][col] = num
                        
                        if sudoku(puzzle):
                            return puzzle
                        
                        puzzle[row][col] = 0
                return False
    return puzzle


def is_valid(puzzle, row, col, num):
    if num in puzzle[row]:
        return False
    
    for i in range(9):
        if puzzle[i][col] == num:
            return False
    
    row_base = (row // 3) * 3
    col_base = (col // 3) * 3
    
    for i in range(3):
        for j in range(3):
            if puzzle[row_base + i][col_base + j] == num:
                return False
    
    return True