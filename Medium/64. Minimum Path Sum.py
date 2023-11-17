class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)-1
        col = len(grid[0])-1
        for i in range(row,-1,-1):
            for j in range(col,-1,-1):
                if i == row and j == col:
                    continue
                minPath = [float('inf'),float('inf')]
                if i != row:
                    minPath[0] = grid[i][j] + grid[i+1][j]
                if j != col:
                    minPath[1] = grid[i][j] + grid[i][j+1]
                grid[i][j] = min(minPath)
        return grid[0][0]       