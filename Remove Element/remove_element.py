from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        match=True
        i=0
        while(match):
            try:
                nums.remove(val)
            except ValueError:
                match=False
        return len(nums)


# Example 1
nums = [3,2,2,3]
val = 3
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

# Example 2
nums = [0,1,2,2,3,0,4,2]
val = 2
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

# #Example 3
nums = [2]
val = 3
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

#Example 4
nums = [1]
val = 1
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)

#Example 5
nums = [3,3]
val = 3
s = Solution()
k = s.removeElement(nums, val)
print(k)
print(nums)


# Runtime
# Details
# 40ms
# Beats 60.23%of users with Python3
# Memory
# Details
# 16.20MB
# Beats 73.57%of users with Python3