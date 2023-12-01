from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        # Iterate and register zero rows and cols
        zero_rows = set()
        zero_cols = set()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        # Iterate to set zero rows and cols
        for r in zero_rows:
            matrix[r] = [0]*n
        for c in zero_cols:
            for r in range(m):
                matrix[r][c] = 0

        return matrix

# Example 1:
matrix = [[1,1,1],[1,0,1],[1,1,1]]
expected = [[1,0,1],[0,0,0],[1,0,1]]
s = Solution()
result = s.setZeroes(matrix)
print(result)
print(result == expected)

# Example 2:
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
expected = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
s = Solution()
result = s.setZeroes(matrix)
print(result)
print(result == expected)