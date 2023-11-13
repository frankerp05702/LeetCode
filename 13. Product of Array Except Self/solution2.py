from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[1]*n
        left_product=1
        for i in range(n):
            out[i]*=left_product
            left_product*=nums[i]

        right_product=1
        for i in range(n-1,-1,-1):
            out[i]*=right_product
            right_product*=nums[i]
        
        return out

# Example 1
nums = [1,2,3,4]
# Output: [24,12,8,6]
s=Solution()
print(s.productExceptSelf(nums))

# Example 2
nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
s=Solution()
print(s.productExceptSelf(nums))