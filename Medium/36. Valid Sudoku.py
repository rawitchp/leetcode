class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hori = [[0] * 9 for _ in range(9)]
        verti = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = 0
                if board[i][j] != ".":
                    num = int(board[i][j])
                if num:
                    if hori[j][num-1] == 1:
                        return False
                    else:
                        hori[j][num-1] = 1
                    if verti[i][num-1] == 1:
                        return False
                    else:
                        verti[i][num-1] = 1
                    y = i//3
                    x = j//3
                    no = y*3 + x
                    if boxes[no][num-1] == 1:
                        return False
                    else:
                        boxes[no][num-1] = 1
        return True