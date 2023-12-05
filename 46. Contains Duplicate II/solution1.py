from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num in index_map and abs(i - index_map[num]) <= k:
                return True
            else:
                index_map[num] = i
        return False


# Example 1:
nums = [1,2,3,1]
k = 3
# Output: true
s = Solution()
result = s.containsNearbyDuplicate(nums, k)
print(result)
print(result == True)

# Example 2:
nums = [1,0,1,1]
k = 1
# Output: true
s = Solution()
result = s.containsNearbyDuplicate(nums, k)
print(result)
print(result == True)


# Example 3:
nums = [1,2,3,1,2,3]
k = 2
# Output: false
s = Solution()
result = s.containsNearbyDuplicate(nums, k)
print(result)
print(result == False)