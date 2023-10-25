class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        traveled = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        island = 0
        def recursion(i,j):
            if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
                return
            if traveled[i][j] == 1:
                return
            traveled[i][j] = 1
            if grid[i][j] == "1":
                recursion(i+1,j)
                recursion(i-1,j)
                recursion(i,j+1)
                recursion(i,j-1)
            return
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and traveled[i][j] == 0:
                    island += 1
                    recursion(i,j)
        return island