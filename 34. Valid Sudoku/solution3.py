from math import trunc
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = []
            column = []
            box = []

            for j in range(9):
                # Check each row
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j])

                # Check each column
                if board[j][i] != ".":
                    if board[j][i] in column:
                        return False
                    column.append(board[j][i])

                # Check each 3x3 box
                box_row, box_col = 3 * (i // 3), 3 * (i % 3)
                if board[box_row + j // 3][box_col + j % 3] != ".":
                    if board[box_row + j // 3][box_col + j % 3] in box:
                        return False
                    box.append(board[box_row + j // 3][box_col + j % 3])

        return True


# Example 1:
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
s = Solution()
result = s.isValidSudoku(board)
print(result)
print(result == True)

# Example 2:

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
s = Solution()
result = s.isValidSudoku(board)
print(result)
print(result == False)