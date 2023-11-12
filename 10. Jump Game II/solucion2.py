from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps, current_max, next_max = 0, 0, 0

        for i in range(n - 1):
            next_max = max(next_max, i + nums[i])

            if i == current_max:
                jumps += 1
                current_max = next_max

        return jumps

# Example 1
nums = [2,3,1,1,4]

s = Solution()
print(s.jump(nums))


# Example 2
nums = [2,3,0,1,4]

s = Solution()
print(s.jump(nums))

# Example 3
nums = [1,2,3]

s = Solution()
print(s.jump(nums))

# Example 4
nums = [6,2,6,4,5,1,2,1]

s = Solution()
print(s.jump(nums))

# Example 5
nums = [1,2,1,1,1]

s = Solution()
print(s.jump(nums))

# Example 6
nums = [10,9,8,7,6,5,4,3,2,1,1,0]

s = Solution()
print(s.jump(nums))

# Example 7
nums = [5,9,8,7,6,5,4,3,2,1,1]

s = Solution()
print(s.jump(nums))