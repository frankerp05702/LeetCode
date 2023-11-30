from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row, col = 0, 0
        direction = True
        forward = True

        left, right, top, bottom = 0, n, 0, m

        spiral = []

        while left < right and top < bottom:
            if direction:
                if forward: # Row forward
                    for col in range(left, right):
                        spiral.append(matrix[row][col])
                    top += 1
                else: # Row backwards
                    for col in range(right - 1, left - 1, -1):
                        spiral.append(matrix[row][col])
                    bottom -= 1
                direction = not direction
            else:
                if forward: # Col Forward
                    for row in range(top, bottom):
                        spiral.append(matrix[row][col])
                    forward = False
                    right -= 1
                else:   # Col Backwards
                    for row in range(bottom - 1, top - 1, -1):
                        spiral.append(matrix[row][col])
                    forward = True
                    left += 1
                direction = not direction
            
        return spiral

# Example 1:
matrix = [[1,2,3],[4,5,6],[7,8,9]]
expected = [1,2,3,6,9,8,7,4,5]
s = Solution()
result = s.spiralOrder(matrix)
print(result)
print(result == expected)

# Example 2:
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
expected = [1,2,3,4,8,12,11,10,9,5,6,7]
s = Solution()
result = s.spiralOrder(matrix)
print(result)
print(result == expected)