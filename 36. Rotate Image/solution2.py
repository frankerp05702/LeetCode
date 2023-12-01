from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        start = 0

        # exchange rows
        i = 0
        while i < n//2:
            temp = matrix[i]
            matrix[i] = matrix[n - 1 - i]
            matrix[n - 1 - i] = temp
            i += 1
            
        # traspose matrix
        for i in range(n):
            start += 1
            for j in range(start, n):
                if i == j: continue
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for r in matrix:
            print(r)

        return matrix

# Example 1:
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
expected = [[7,4,1],
            [8,5,2],
            [9,6,3]]
s = Solution()
result = s.rotate(matrix)
print(result)
print(result == expected)

# Example 2:
matrix = [[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]]
expected = [[15,13,2,5],
            [14,3,4,1],
            [12,6,8,9],
            [16,7,10,11]]
s = Solution()
result = s.rotate(matrix)
print(result)
print(result == expected)