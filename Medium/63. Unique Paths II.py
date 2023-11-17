class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        if obstacleGrid[row-1][col-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        if len(obstacleGrid) == 1:
            return 1
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = '#'
        for i in range(row-2,-1,-1):
            if obstacleGrid[i][col-1] != '#':
                obstacleGrid[i][col-1] = 1
            else:
                break
        for j in range(col-2,-1,-1):
            if obstacleGrid[row-1][j] != '#':
                obstacleGrid[row-1][j] = 1
            else:
                break
        for i in range(row-2,-1,-1):
            for j in range(col-2,-1,-1):
                if obstacleGrid[i][j] == '#':
                    continue
                if obstacleGrid[i][j+1] != '#':
                    obstacleGrid[i][j] += obstacleGrid[i][j+1]
                if obstacleGrid[i+1][j] != '#':
                    obstacleGrid[i][j] += obstacleGrid[i+1][j]
        return obstacleGrid[0][0]