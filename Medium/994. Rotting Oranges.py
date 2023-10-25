class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        fresh = 0
        rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        minute = 0
        while rotten and fresh > 0:
            minute += 1
            for _ in range(len(rotten)):
                i,j = rotten.pop(0)
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    x = i + dx
                    y = j + dy
                    if x < 0 or y < 0 or x >=len(grid) or y >= len(grid[0]):
                        continue
                    if grid[x][y] == 0 or grid[x][y] == 2:
                        continue
                    else:
                        fresh -= 1
                        grid[x][y] = 2
                        rotten.append([x,y])
        return minute if fresh == 0 else -1