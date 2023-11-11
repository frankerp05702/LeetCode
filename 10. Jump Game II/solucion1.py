from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        position=len(nums)-1
        jumps=0
        farthest_i=0
        while position>0:
            # Find the farthest position that can reach
            for i in range(position-1,position-1000,-1):
                reachable=i+nums[i]
                if reachable>=position:
                    farthest_i=i
                if i==0: break
            position=farthest_i
            jumps+=1
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