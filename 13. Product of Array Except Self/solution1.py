from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        out=[1]
        for i in range(1,n):
            out.append(out[i-1]*nums[i-1])
        cumul=1
        for j in range(n-2,-1,-1):
            cumul*=nums[j+1]
            out[j]=out[j]*cumul
        
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