class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]* n] * m

        for i in range(m):
            for j in range(n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1] if (i > 0 and j > 0) else 1
        
        # print(grid)
        return grid[m-1][n-1]