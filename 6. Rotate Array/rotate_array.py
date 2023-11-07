from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        top_elem=len(nums)-1
        for i in range(k):
            nums.insert(0,nums.pop(top_elem))

# Example 1:
nums = [1,2,3,4,5,6,7]
k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
s = Solution()
s.rotate(nums, k)
print(nums)

# Example 2:
nums = [-1,-100,3,99]
k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
s = Solution()
s.rotate(nums, k)
print(nums)

# Runtime
# Details
# 147ms
# Beats 74.03%of users with Python3
# Memory
# Details
# 17.74MB
# Beats 74.09%of users with Python3