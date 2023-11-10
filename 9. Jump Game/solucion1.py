from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True

        last_zero = -1
        zeros = nums.count(0)
        if not zeros:
            return True

        if nums[0]==0:
            return False

        for times in range(zeros):
            zero_index = nums.index(0,last_zero+1)
            if zero_index==len(nums)-1:
                return True
            for i in range(zero_index):
                if i+nums[i]>zero_index:
                    last_zero=zero_index
                    break
                if i==zero_index-1:
                    return False
                
        return True

# Example 1
nums = [2,3,1,1,4]

s = Solution()
print(s.canJump(nums))


# Example 2
nums = [3,2,1,0,4]

s = Solution()
print(s.canJump(nums))

# Example 3
nums = [0]

s = Solution()
print(s.canJump(nums))

# Example 4
nums = [1,0]

s = Solution()
print(s.canJump(nums))

# Example 5
nums = [0,1]

s = Solution()
print(s.canJump(nums))

# Example 6
nums = [2,0,0]

s = Solution()
print(s.canJump(nums))

# Example 7
nums = [2,0,2]

s = Solution()
print(s.canJump(nums))

# Example 8
nums = [2,0,0,0,2,0,0,0]

s = Solution()
print(s.canJump(nums))

# Example 9
nums = [3,0,0,0]

s = Solution()
print(s.canJump(nums))