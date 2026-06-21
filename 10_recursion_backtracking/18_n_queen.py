class Solution:
    def solve(self, col, board:list[list[str]], n, leftRow:list[int], upperDiagonal:list[int], lowerDiagonal:list[int], ans:list[str]):
        if col == n:
            ans.append(["".join(row) for row in board])
            return

        for row in range(n):
            if leftRow[row] == 0 and lowerDiagonal[row + col] == 0 and upperDiagonal[n - 1 + col - row] == 0:
                #place queen
                board[row][col] = 'Q'
                leftRow[row] = lowerDiagonal[row + col] = upperDiagonal[n - 1 + col - row] = 1

                self.solve(col + 1, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)

                board[row][col] = '.'
                leftRow[row] = lowerDiagonal[row + col] = upperDiagonal[n - 1 + col - row] = 0
            
    def solve_n_queens(self, n:int):
       ans = []
       board = [['.' for _ in range(n)] for _ in range(n)]
       leftRow = [0] * n
       lowerDiagonal = [0] * (2*n-1)
       upperDiagonal = [0] * (2*n-1)
       self.solve(0, board, n, leftRow, upperDiagonal, lowerDiagonal, ans)
       return ans


sol = Solution()
answer = sol.solve_n_queens(4)
for board in answer:
    for row in board:        
        print(row)
    print()