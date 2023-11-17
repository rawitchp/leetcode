class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)-1
        col = len(matrix[0])-1
        max_area = 0
        for i in range(row+1):
            matrix[i][col] = int(matrix[i][col])
            if matrix[i][col]:
                max_area = 1
        for j in range(col+1):
            matrix[row][j] = int(matrix[row][j])
            if matrix[row][j]:
                max_area = 1
        # for i in matrix:
        #     print(i)
        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                # print(i,j)
                if matrix[i][j] == '1':
                    matrix[i][j] = min(matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1]) + 1
                    max_area = max(max_area,matrix[i][j])
                else:
                    matrix[i][j] = int(matrix[i][j])
        # for i in matrix:
        #     print(i)
        return max_area**2