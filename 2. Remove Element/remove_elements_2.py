from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last_j=len(nums)-1
        for i in range(len(nums)):
            if nums[i]==val:
                found=None
                # Find not val and assign it here
                for j in range(last_j,i+1,-1):
                    found=None
                    elem = nums[j]
                    if elem==val:
                        nums[j]='_'
                        continue
                    else:
                        found=elem
                        last_j=j-1
                        nums[j]='_'
                        break
                if found==None:
                    nums[i]="_"
                else:
                    nums[i]=found

        return len(nums)-nums.count("_")


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
# 32ms
# Beats 94.57%of users with Python3
# Memory
# Details
# 16.35MB
# Beats 9.20%of users with Python3