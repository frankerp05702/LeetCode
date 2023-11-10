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

        position=len(nums)-2
        while position>0:
            if nums[position]>0:
                position-=1
            else:
                # Found a zero, is it jumpable?
                for i in range(position,-1,-1):
                    # If nums[i] can jump the last zero, keep looking for reachable positions from there
                    if i+nums[i]>position:
                        position=i
                        break
                    # If last zero is not jumpable, return false
                    if i==0:
                        return False
        
        # If I got this far, means everything is reachable
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