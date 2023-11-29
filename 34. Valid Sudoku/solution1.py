from math import trunc
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        h_count, v_count, q_count = ["."]*9, ["."]*9, ["."]*9

        for i in range(n):
            for j in range(n):
                char = 10
                h_count[i] = { char: 0 }
                v_count[j] = { char: 0 }
                iq = trunc(i/3)
                jq = trunc(j/3)
                q_count[3*iq + jq] = { char: 0 }


        for i in range(n):
            for j in range(n):
                char = board[i][j]
                if char == ".": continue
                if char in h_count[i] and h_count[i][char] >= 1: return False
                else: h_count[i][char] = 1
                if char in v_count[j] and v_count[j][char] >= 1: return False
                else: v_count[j][char] = 1
                iq = trunc(i/3)
                jq = trunc(j/3)
                if char in q_count[3*iq + jq] and q_count[3*iq + jq][char] >= 1: return False
                else: q_count[3*iq + jq][char] = 1

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