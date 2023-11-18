from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped = 0
        wall = False
        counting = False

        if n <= 2: return 0

        max_height = max(height)

        for level in range(1, max_height + 1):
            wall = False
            counting = False
            count = 0
            for h in height:
                if h >= level:
                    if counting: 
                        trapped += count
                    wall = True
                    counting = False
                    count = 0
                    continue
                if h < level and wall:
                    counting = True
                    wall = False
                if h < level and counting:
                    count += 1     

        return trapped

# Example 1:

height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
s = Solution()
result = s.trap(height)
print(result)
print(result==6)

# Example 2:

height = [4,2,0,3,2,5]
# Output: 9
s = Solution()
result = s.trap(height)
print(result)
print(result==9)

height = [0,2,0]
# Output: 0
s = Solution()
result = s.trap(height)
print(result)
print(result==0)

height = [4,2,3]
# Output: 1
s = Solution()
result = s.trap(height)
print(result)
print(result==1)

height = [5,4,1,2]
# Output: 1
s = Solution()
result = s.trap(height)
print(result)
print(result==1)