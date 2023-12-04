from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if not nums or n < 2: return []

        for i in range(n - 1):
            j = i + 1
            while j < n:
                a = nums[i]
                b = nums[j]
                if a + b == target:
                    return [i, j]
                j += 1

        return []



# Example 1:
nums = [2,7,11,15]
target = 9
expected = [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 2:
nums = [3,2,4]
target = 6
expected = [1,2]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 3:
nums = [3,3]
target = 6
expected = [0,1]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 4:
nums = [3,2,3]
target = 6
expected = [0,2]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 5:
nums = [2,5,5,11]
target = 10
expected = [1,2]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)

# Example 5:
nums = [0,4,3,0]
target = 0
expected = [0,3]
s = Solution()
result = s.twoSum(nums, target)
print(result)
print(result == expected)