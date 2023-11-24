from math import trunc
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums: return 1
        if max(nums) >= target: return 1
        n = len(nums)

        left = 0
        current_sum = 0
        min_length = float('inf')

        for right, num in enumerate(nums):
            current_sum += num

            while current_sum >= target:
                min_length = min(min_length, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return min_length if min_length != float('inf') else 0
             

# Example 1:
target = 7
nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
s = Solution()
result = s.minSubArrayLen(target, nums)
print(result)
print(result == 2)


# Example 2:

target = 4
nums = [1,4,4]
# Output: 1
s = Solution()
result = s.minSubArrayLen(target, nums)
print(result)
print(result == 1)

# Example 3:

target = 11
nums = [1,1,1,1,1,1,1,1]
# Output: 0
s = Solution()
result = s.minSubArrayLen(target, nums)
print(result)
print(result == 0)

# Example 4:

target = 15
nums = [1,2,3,4,5]
# Output: 5
s = Solution()
result = s.minSubArrayLen(target, nums)
print(result)
print(result == 5)

# Example 5:

target = 213
nums = [12,28,83,4,25,26,25,2,25,25,25,12]
# Output: 8
s = Solution()
result = s.minSubArrayLen(target, nums)
print(result)
print(result == 8)