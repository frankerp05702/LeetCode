import bisect
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0

        # Create a cumulative sum array
        cum_sum = [0]
        for num in nums:
            cum_sum.append(cum_sum[-1] + num)

        min_length = float('inf')

        for i in range(len(cum_sum)):
            end = bisect.bisect_left(cum_sum, cum_sum[i] + target)
            if end != len(cum_sum):
                min_length = min(min_length, end - i)

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