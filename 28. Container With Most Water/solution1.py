from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        i, j = 0, n - 1
        max_area, max_left, max_right = 0, 0, 0
        
        while i < j:
            base = j - i
            h = min(height[i], height[j])
            area = base * h
            max_area = area if area > max_area else max_area
            if height[i] < height[j]: 
                i += 1; 
            else:
                j -= 1

        return max_area


# Example 1:
height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
s = Solution()
result = s.maxArea(height)
print(result)
print(result == 49)

# Example 2:
height = [1,1]
# Output: 1
s = Solution()
result = s.maxArea(height)
print(result)
print(result == 1)