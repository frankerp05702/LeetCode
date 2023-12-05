from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        longest = 0
        for i in range(n):
            if i > 0 and nums[i] - nums[i - 1] == 1:
                consec += 1
            else:
                consec = 1
            if consec > longest:
                longest = consec
        return longest



# Example 1:
nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
s = Solution()
result = s.longestConsecutive(nums)
print(result)
print(result == 4)

# Example 2:
nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
s = Solution()
result = s.longestConsecutive(nums)
print(result)
print(result == 9)