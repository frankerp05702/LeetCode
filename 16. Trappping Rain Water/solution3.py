from typing import List


class Solution:
    def water_trapped(self, height: List[int], start: int, stop: int):
        trapped = 0
        water_height = min(height[start], height[stop])

        if stop - start < 2: return 0

        for i in range(start+1,stop):
            trapped += water_height - height[i]

        return trapped
    def trap(self, height: List[int]) -> int:
        n = len(height)
        trapped = 0
        h_dict = {}
        walls = []

        if n <= 2: return 0

        for i, h in enumerate(height):
            if h > 0: h_dict[h] = []
        
        # Create arrays for heights
        for i, h in enumerate(height):
            if h > 0: h_dict[h].append(i)

        # Sort from higher to lower heights
        sorted = list(h_dict.keys())
        sorted.sort(reverse=True)


        min_index = 100000
        max_index = 0
        # Higher walls can trap water with lower walls
        for i in range(len(sorted)):
            for wall_index in h_dict[sorted[i]]:
                if len(walls) == 0:
                    walls.append(wall_index)
                else:
                    if wall_index < min_index or wall_index > max_index:
                        walls.append(wall_index)
                if wall_index < min_index: min_index = wall_index
                if wall_index > max_index: max_index = wall_index

        # Sort walls in order of appearance
        walls.sort()

        if len(walls) < 2: return 0

        # From calculate trapped water between every wall
        if len(walls) < 3:
            if walls[1] - walls[0] == 0: return 0
            trapped += self.water_trapped(height, walls[0], walls[1])
        else:
            for i in range(len(walls)-1):
                trapped += self.water_trapped(height, walls[i], walls[i+1])

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