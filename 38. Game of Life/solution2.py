from typing import List


class Solution:
    def update_neig_counts(self, r: int, c: int, count, m: int, n: int):
        for row in range(r - 1, r + 2):
            for col in range(c - 1, c + 2):
                if row < 0 or row >= m or col < 0 or col >= n or (row == r and col == c):
                    continue
                if (row,col) not in count:
                    count[(row,col)] = 1
                else:
                    count[(row,col)] += 1
        return
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])
        count = {}

        current_row = []

        for r in range(m):
            for c in range(n):
                if board[r][c] == 1:
                    self.update_neig_counts(r, c, count, m, n)

        for r in range(m):
            previous_row = current_row
            current_row = []
            for c in range(n):
                if board[r][c] == 0:
                    if (r, c) in count and count[(r, c)] == 3: current_row.append(1)
                    else: current_row.append(0)
                else:
                    if (r, c) in count and (count[(r, c)] == 2 or count[(r, c)] == 3): current_row.append(board[r][c])
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

# Example 3:
board = [[0]]
expected = [[0]]
s = Solution()
result = s.gameOfLife(board)
print(board)
print(board == expected)