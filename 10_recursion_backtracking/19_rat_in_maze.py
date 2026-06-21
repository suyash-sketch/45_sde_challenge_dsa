class Solution:
    def is_safe(self, x, y, n, maze:list[list[int]], visited:list[list[int]]):
        return (0 <= x < n and 0 <= y < n and maze[x][y] == 1 and visited[x][y] == 0)

    def solve(self, x,y, n, maze:list[list[int]], visited: list[list[int]], path:str, res:list[str]):
        if x == n -1 and y == -1: #destination reached
            res.append(path)
            return

        visited[x][y] == 1
        #try moving down
        if self.is_safe(x + 1, y, n, maze, visited):
            self.solve(x+1,y, n, maze, visited,path + "D", res)

        #try moving left
        if self.is_safe(x, y - 1, n, maze, visited):
          self.solve(x, y - 1, n, maze, visited, path + "L", res)
        
        #try moving right
        if self.is_safe(x, y + 1, n, maze, visited):
            self.solve(x, y + 1, n, maze, visited, path + "R", res)

        # try moving up
        if self.is_safe(x - 1, y, n, maze, visited):
            self.solve(x - 1, y, n, maze, visited, path + "U", res)

        visited[x][y] = 0

        
    def find_path(self, grid: list[list[int]]):
        n = len(grid)
        res = []
        visited = [[0]*n for _ in range(n)]
        if grid[0][0]  == 1:
            self.solve(0,0,n, grid, visited, "", res)
        return res
        