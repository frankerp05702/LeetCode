from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> List[int]:
        matrix[:] = [list(x[::-1]) for x in list(zip(*matrix))]

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