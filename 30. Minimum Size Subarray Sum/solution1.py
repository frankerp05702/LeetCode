from math import trunc
from typing import List


class Solution:
    def sum_subarray(self, nums: List[int], start: int, lenn: int) -> int:
        result = 0
        for i in range(start, start + lenn):
            result += nums[i]
        return result
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums: return 1
        if max(nums) >= target: return 1
        n = len(nums)        
        for lenn in range(2, n + 1):
            for i in range(n - lenn + 1):
                current_sum = self.sum_subarray(nums, i, lenn)
                if current_sum >= target: 
                    return lenn
        return 0
             

# # Example 1:
# target = 7
# nums = [2,3,1,2,4,3]
# # Output: 2
# # Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# s = Solution()
# result = s.minSubArrayLen(target, nums)
# print(result)
# print(result == 2)


# # Example 2:

# target = 4
# nums = [1,4,4]
# # Output: 1
# s = Solution()
# result = s.minSubArrayLen(target, nums)
# print(result)
# print(result == 1)

# # Example 3:

# target = 11
# nums = [1,1,1,1,1,1,1,1]
# # Output: 0
# s = Solution()
# result = s.minSubArrayLen(target, nums)
# print(result)
# print(result == 0)

# Example 4:

target = 15
nums = [1,2,3,4,5]
# Output: 5
s = Solution()
result = s.minSubArrayLen(target, nums)
print(result)
print(result == 5)