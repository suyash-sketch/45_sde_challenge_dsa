class Solution:
    def solve_soduko(self, board: list[list[str]]):
        empty_cells = []
        for i in range(9):
            for j in range(9):
        if board[i][j] == '.':
                    empty_cells.append((i,j))

        def is_valid(row:int, col:int, char):
            for i in range(9):
                #check row
                if board[row][i] == char:
                    return False

                if board[i][col] == char:
                    return False

                box_row = 3 * (row // 3) + i // 3
                box_col = 3 * (col // 3) + i % 3
                if board[box_row][box_col] == char:
                    return False

            return True
        
        def backtrack(idx):
            if idx == len(empty_cells):
              return True
            
            row, col = empty_cells[idx]

            for c in map(str, range(1,10)):
                if is_valid(row, col, c):
                    board[row][col] = c

                    if backtrack(idx + 1):
                        return True

                    board[row][col] = '.'

            return False

        backtrack(0)
                        
                


                
    # def isValid(self, board: list[list[str]],row : int, col : int, c : str):
    #     for i in range(9):
    #         if board[i][col] == c:
    #             return False

    #     for j in range(9):
    #         if board[row][j] == c:
    #             return False

    #     box_row_start = 3 * (row // 3)
    #     box_col_start = 3 * (col // 3)

    #     for i in range(3):
    #         for j in range(3):
    #             if board[box_row_start+i][box_col_start+j] == c:
    #                 return False

    #     return True

    # def solve_sudoku(self, board: list[list[str]]):
    #     for i in range(9):
    #         for j in range(9):

    #             if board[i][j] == '.':
    #                 for c in map(str, range(1,10)):
    #                     if self.isValid(board, i,j, c):
    #                         board[i][j] = c

    #                         if self.solve_sudoku(board):
    #                             return True

    #                         board[i][j] = '.'

    #                 return False

    #     return True


                            