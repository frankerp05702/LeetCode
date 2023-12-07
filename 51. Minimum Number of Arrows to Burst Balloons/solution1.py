from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])  # Sort by end coordinates

        arrows = 1
        end = points[0][1]

        for start, balloon_end in points[1:]:
            if start > end:
                arrows += 1
                end = balloon_end

        return arrows


# Example 1:
points = [[10,16],[2,8],[1,6],[7,12]]
expected = 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
# - Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
s = Solution()
result = s.findMinArrowShots(points)
print(result)
print(result == expected)


# Example 2:
points = [[1,2],[3,4],[5,6],[7,8]]
expected = 4
# Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
s = Solution()
result = s.findMinArrowShots(points)
print(result)
print(result == expected)


# Example 3:
points = [[1,2],[2,3],[3,4],[4,5]]
expected = 2
# Explanation: The balloons can be burst by 2 arrows:
# - Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
# - Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
s = Solution()
result = s.findMinArrowShots(points)
print(result)
print(result == expected)

# Example 4:
points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
expected = 2
s = Solution()
result = s.findMinArrowShots(points)
print(result)
print(result == expected)

