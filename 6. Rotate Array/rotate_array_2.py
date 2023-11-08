from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # With list comprehension
        lenn=len(nums)
        temp=[]
        for i in range(lenn):
            pos = lenn-k+i
            while pos<0:
                pos=pos+lenn
            if pos>lenn-1: pos=pos%lenn
            temp.append(nums[pos])
        for i in range(lenn):
            nums[i]=temp[i]

# # Example 1:
# nums = [1,2,3,4,5,6,7]
# k = 3
# # Output: [5,6,7,1,2,3,4]
# # Explanation:
# # rotate 1 steps to the right: [7,1,2,3,4,5,6]
# # rotate 2 steps to the right: [6,7,1,2,3,4,5]
# # rotate 3 steps to the right: [5,6,7,1,2,3,4]
# s = Solution()
# s.rotate(nums, k)
# print(nums)

# # Example 2:
# nums = [-1,-100,3,99]
# k = 2
# # Output: [3,99,-1,-100]
# # Explanation: 
# # rotate 1 steps to the right: [99,-1,-100,3]
# # rotate 2 steps to the right: [3,99,-1,-100]
# s = Solution()
# s.rotate(nums, k)
# print(nums)

# Example 3:
nums = [1,2,3]
k = 4
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
s = Solution()
s.rotate(nums, k)
print(nums)

# Runtime
# Details
# 194ms
# Beats 34.80%of users with Python3
# Memory
# Details
# 27.66MB
# Beats 75.47%of users with Python3