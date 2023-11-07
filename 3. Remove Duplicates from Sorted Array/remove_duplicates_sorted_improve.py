from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # As numbers are ordered
        for i in range(len(nums)-1,0,-1):
            if(nums[i]==nums[i-1]):
                nums.pop(i)        

        return len(nums)


# Example 1:
nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)

# Example 2:
nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)

# Example 3
nums = [-1,0,0,0,0,3,3]
s = Solution()
k = s.removeDuplicates(nums)
print(k)
print(nums)

# Runtime
# Details
# 78ms
# Beats 88.67%of users with Python3
# Memory
# Details
# 17.81MB
# Beats 62.74%of users with Python3