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
        lenn_asc, lenn_desc = 2, n
        desc_len_found = False
        desc_was_finding = False
        min_len = n
        while lenn_asc <= lenn_desc:
            for j in range(n - lenn_desc + 1):
                current_sum = self.sum_subarray(nums, j, lenn_desc)
                if current_sum >= target:
                    desc_len_found = True
                    min_len = lenn_desc if lenn_desc < min_len else min_len
                else:
                    if lenn_desc == n:
                        return 0
            if not desc_len_found:
                if desc_was_finding:
                    return min_len
            else:
                desc_len_found = False
                desc_was_finding = True

            for i in range(n - lenn_asc + 1):
                current_sum = self.sum_subarray(nums, i, lenn_asc)
                if current_sum >= target: 
                    return lenn_asc
            
            lenn_asc += 1
            lenn_desc -= 1
        return 0
             

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