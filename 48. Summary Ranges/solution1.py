from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        ranges = []
        current_range = ""
        for i, num in enumerate(nums):
            if not current_range:
                current_range = str(num)
            if i < n - 1 and nums[i + 1] - num == 1:
                if "->" not in current_range:
                    current_range += "->"
            else:
                if current_range[-1] == ">":
                    current_range += str(num)
                ranges.append(current_range)
                current_range = ""
        return ranges

# Example 1:
nums = [0,1,2,4,5,7]
expected = ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
s = Solution()
result = s.summaryRanges(nums)
print(result)
print(result == expected)


# Example 2:
nums = [0,2,3,4,6,8,9]
expected = ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"
s = Solution()
result = s.summaryRanges(nums)
print(result)
print(result == expected)