from typing import List


class Solution:
    def count_neighboors(self, board: List[List[int]], r: int, c: int, m: int, n: int) -> int:
        count = 0
        for row in range(r - 1, r + 2):
            for col in range(c - 1, c + 2):
                if row < 0 or row >= m or col < 0 or col >= n or (row == r and col == c):
                    continue
                count += board[row][col]
        return count
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        current_row = []

        for r in range(m):
            previous_row = current_row
            current_row = []
            for c in range(n):
                count = self.count_neighboors(board, r, c, m, n)
                if count == 2: current_row.append(board[r][c])
                elif count == 3: current_row.append(1)
                else: current_row.append(0)
            if r >= 1: board[r - 1] = previous_row
            if r == m - 1: board[r] = current_row

        return

# Example 1:
board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
s = Solution()
result = s.gameOfLife(board)
print(board)
print(board == expected)

# Example 2:
board = [[1,1],[1,0]]
expected = [[1,1],[1,1]]
s = Solution()
result = s.gameOfLife(board)
print(board)
print(board == expected)